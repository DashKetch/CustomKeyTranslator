import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Directory where language JSON files are stored
LANG_DIR = BASE_DIR / "languages"

# Default configuration settings
DEFAULT_LANG = "es"
ENCODING = "utf-8"

def get_language_file_path(lang_code: str) -> Path:
    """Returns the full path for a specific language code."""
    return LANG_DIR / f"{lang_code}.json"