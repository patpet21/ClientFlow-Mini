"""Create buyer and seller ZIPs from the checked-in ClientFlow Mini files."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(parents=True, exist_ok=True)
buyer = [
    ("ClientFlow-Mini.html", "ClientFlow-Mini.html"),
    ("docs/START-HERE-EN.txt", "START-HERE-EN.txt"),
    ("docs/START-HERE-IT.txt", "START-HERE-IT.txt"),
    ("docs/BUYER-LICENSE-DRAFT.txt", "BUYER-LICENSE-DRAFT.txt"),
]
seller = buyer + [
    ("docs/SALES-COPY-READY.md", "SALES-COPY-READY.md"),
    *[(f"assets/{name}", name) for name in (
        "preview-dashboard.png", "preview-clients.png", "preview-quotes.png", "preview-mobile.png"
    )],
]
for name, files in (("ClientFlow-Mini-BUYER-PACK.zip", buyer), ("ClientFlow-Mini-FULL-SELLER-KIT.zip", seller)):
    missing = [src for src, _ in files if not (ROOT / src).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing sources for {name}: {missing}")
    with ZipFile(DIST / name, "w", compression=ZIP_DEFLATED, compresslevel=8) as bundle:
        for src, target in files:
            bundle.write(ROOT / src, target)
    print(f"Created {DIST / name}")
