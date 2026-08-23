import json
from pathlib import Path

from utils.logging import log_error


def load_data(file_path):
    path = Path(file_path)
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        log_error(f"Missing data file: {path}")
        return []
    except json.JSONDecodeError as error:
        log_error(f"Corrupted JSON in {path}: {error}")
        return []
    except OSError as error:
        log_error(f"Could not read {path}: {error}")
        return []
    else:
        if not isinstance(data, list):
            log_error(f"Invalid data format in {path}; expected a list")
            return []
        return data


def save_data(file_path, data):
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except (OSError, TypeError) as error:
        log_error(f"Could not save {path}: {error}")
        return False
    else:
        return True
