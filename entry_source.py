import os
from pathlib import Path

FINAL_WIFI_NAME = "HeKnelt_SheGaveWrongPassword"


def emit(name: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(name, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_WIFI_NAME)
