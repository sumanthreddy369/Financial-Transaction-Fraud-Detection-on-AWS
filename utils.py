from pathlib import Path
import json


def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def save_json(data: dict, path: str) -> None:
    ensure_dir(str(Path(path).parent))
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)
