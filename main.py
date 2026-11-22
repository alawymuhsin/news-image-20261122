"""Copy the front-page image to the output directory.

The entry is a single image (entry.png) summing up the world news of
Sunday 22 November 2026. The program runs with no network, so it simply
copies the image that ships in this repository to /output/entry.png.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
if not SOURCE.is_file():
    raise SystemExit(f"entry image missing: {SOURCE}")
shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")
written = OUTPUT_DIR / "entry.png"
if written.stat().st_size != SOURCE.stat().st_size:
    raise SystemExit(
        f"copy incomplete: wrote {written.stat().st_size} bytes, "
        f"expected {SOURCE.stat().st_size}"
    )
print(f"wrote {written} ({SOURCE.stat().st_size} bytes)")
