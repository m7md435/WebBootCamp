from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "logs.txt"


def log_error(message):
    try:
        with LOG_FILE.open("a", encoding="utf-8") as file:
            file.write(f"{message}\n")
    except OSError:
        pass
