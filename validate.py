import json
import logging
from typing import Dict, Any, Union, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def validate_json_structure(data: Dict[str, Any]) -> bool:
    """
    Validates the structure of the language dictionary.

    Requirements:
    1. Must contain the key 'language'.
    2. Values must be strings or lists of strings.
    """
    if "language" not in data:
        logging.error("Validation Failed: Missing required key 'language'.")
        return False

    for key, value in data.items():
        if key == "language":
            continue

        # Check if value is string
        if isinstance(value, str):
            continue

        # Check if value is a list of strings
        if isinstance(value, list):
            if not all(isinstance(item, str) for item in value):
                logging.error(f"Validation Failed: Key '{key}' contains non-string items in list.")
                return False
        else:
            logging.error(f"Validation Failed: Key '{key}' must be a string or list of strings.")
            return False

    return True


def load_and_validate(filepath: str) -> Union[Dict, None]:
    """
    Loads a JSON file and runs validation logic.
    Returns the dictionary if valid, None otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if validate_json_structure(data):
            return data
        return None

    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON format in {filepath}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error validating {filepath}: {e}")
        return None