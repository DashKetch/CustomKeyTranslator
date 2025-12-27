import sys
import os
from pathlib import Path

def get_base_path():
    """
    Determine the correct path for resources whether running
    as a script or as a compiled PyInstaller executable.
    """
    if getattr(sys, 'frozen', False):
        # If running as a compiled exe, look in the temporary sys._MEIPASS folder
        return Path(sys._MEIPASS)
    else:
        # If running as a script, look in the file's current directory
        return Path(__file__).resolve().parent

# Set BASE_DIR using the logic above
BASE_DIR = get_base_path()
LANG_DIR = BASE_DIR / "languages"

DEFAULT_LANG = "es"

def get_language_file_path(lang_code: str) -> Path:
    return LANG_DIR / f"{lang_code}.json"