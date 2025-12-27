import sys
from cli import parse_args
from translate import Translator

def main():
    """
    Main application entry point.
    """
    # 1. Parse Arguments
    args = parse_args()

    # 2. Initialize Translator
    print(f"--- Initializing Translator for language: {args.lang} ---")
    translator = Translator(args.lang)

    # 3. Perform Translation
    original_text = args.text
    result = translator.translate_text(original_text)

    # 4. Output Result
    print("\nOriginal:", original_text)
    print("Translated:", result)
    print("\n------------------------------------------------")

if __name__ == "__main__":
    main()