#!/usr/bin/env python3
"""Rendert Office-Aktenstücke layoutgetreu und reproduzierbar als PDF.

Die bisherige reine Textextraktion bleibt in den aufrufenden Buildern als
Fallback erhalten. Ist LibreOffice verfügbar, bleiben dagegen Briefköpfe,
Kopf- und Fußzeilen, Tabellengeometrie und Seitenumbrüche erhalten.
"""

from __future__ import annotations

import hashlib
import io
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter


OFFICE_EXTS = {"docx", "odt"}
FIXED_DATE = "D:20000101000000Z"


class OfficeRenderError(RuntimeError):
    """Eine native Office-Konvertierung ist fehlgeschlagen."""


def valid_office_container(path: Path) -> bool:
    """Verhindert, dass Office beliebigen Text mit falscher Endung rendert."""
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
    except (OSError, zipfile.BadZipFile):
        return False
    ext = path.suffix.lower()
    if ext == ".docx":
        return "[Content_Types].xml" in names and "word/document.xml" in names
    if ext == ".odt":
        return "mimetype" in names and "content.xml" in names
    return False


def office_binary() -> str | None:
    configured = os.environ.get("SOFFICE", "").strip()
    if configured:
        return configured
    return shutil.which("soffice") or shutil.which("libreoffice")


def normalize_pdf(data: bytes, title: str) -> bytes:
    """Entfernt variable Office-Metadaten und erzeugt stabile PDF-Bytes."""
    try:
        pages = list(PdfReader(io.BytesIO(data)).pages)
    except Exception as exc:
        raise OfficeRenderError(f"Office-Ausgabe ist kein lesbares PDF: {exc}") from exc
    if not pages:
        raise OfficeRenderError("Office-Ausgabe enthält keine Seite")

    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "Kanzleiakte",
            "/CreationDate": FIXED_DATE,
            "/ModDate": FIXED_DATE,
        }
    )
    out = io.BytesIO()
    writer.write(out)
    return out.getvalue()


def render_office_batch(paths: list[Path]) -> dict[Path, bytes]:
    """Konvertiert mehrere Office-Dateien in einem isolierten Office-Lauf.

    Ein leerer Rückgabewert bedeutet, dass LibreOffice nicht installiert ist.
    Fehlende Ausgaben einzelner defekter Dateien bleiben ebenfalls aus der
    Abbildung heraus; der aufrufende Builder verwendet dann seinen strengen
    Parser-Fallback und meldet einen nachvollziehbaren Dokumentfehler.
    """
    candidates = [
        p
        for p in paths
        if p.suffix.lower().lstrip(".") in OFFICE_EXTS and valid_office_container(p)
    ]
    if not candidates:
        return {}
    binary = office_binary()
    if not binary:
        return {}

    with tempfile.TemporaryDirectory(prefix="testakte-office-") as tmp:
        root = Path(tmp)
        source_dir = root / "source"
        output_dir = root / "pdf"
        profile_dir = root / "profile"
        home_dir = root / "home"
        for directory in (source_dir, output_dir, profile_dir, home_dir):
            directory.mkdir()

        staged: dict[Path, Path] = {}
        for index, source in enumerate(candidates):
            digest = hashlib.sha256(str(source.resolve()).encode("utf-8")).hexdigest()[:10]
            target = source_dir / f"{index:04d}-{digest}{source.suffix.lower()}"
            shutil.copyfile(source, target)
            staged[source] = target

        command = [
            binary,
            f"-env:UserInstallation={profile_dir.resolve().as_uri()}",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(output_dir),
            *[str(path) for path in staged.values()],
        ]
        env = os.environ.copy()
        env["HOME"] = str(home_dir)
        timeout = max(90, min(900, 20 + len(staged) * 15))
        try:
            completed = subprocess.run(
                command,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise OfficeRenderError(
                f"LibreOffice-Konvertierung nach {timeout} Sekunden abgebrochen"
            ) from exc

        rendered: dict[Path, bytes] = {}
        for source, stage in staged.items():
            pdf = output_dir / f"{stage.stem}.pdf"
            if not pdf.is_file() or pdf.stat().st_size == 0:
                continue
            rendered[source] = normalize_pdf(pdf.read_bytes(), source.name)

        if completed.returncode != 0 and not rendered:
            stderr = completed.stderr.decode("utf-8", errors="replace").strip()
            raise OfficeRenderError(
                f"LibreOffice-Konvertierung fehlgeschlagen: {stderr[:500]}"
            )
        return rendered


def render_office(path: Path) -> bytes | None:
    """Konvertiert eine Office-Datei; ohne Office-Programm wird None geliefert."""
    return render_office_batch([path]).get(path)
