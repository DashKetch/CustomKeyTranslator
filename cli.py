import argparse
from config import DEFAULT_LANG

def parse_args():
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Custom Language Translator: Translate text using local JSON files."
    )

    parser.add_argument(
        "--lang",
        type=str,
        default=DEFAULT_LANG,
        help=f"Target language code (filename without extension). Default: {DEFAULT_LANG}"
    )

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="The text string to translate."
    )

    return parser.parse_args()