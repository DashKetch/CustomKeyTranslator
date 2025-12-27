import sys
from cli import parse_args
from translate import Translator
import config  # Import config to access language listing


def main():
    if len(sys.argv) > 1:
        args = parse_args()
        lang = args.lang
        text = args.text
    else:
        print("--- Custom Language Translator ---")

        # Display available languages
        available = config.list_available_languages()
        if available:
            print(f"Available languages: {', '.join(available)}")
        else:
            print("No language files found in the 'languages' directory.")

        lang = input("Enter target language: ").strip()
        text = input("Enter text to translate: ").strip()

    # Initialize and Translate
    translator = Translator(lang)

    # Check if translator actually loaded mappings
    if not translator.mappings and lang not in ["en", "english"]:
        print(f"Note: No dictionary found for '{lang}'. Text will remain unchanged.")

    result = translator.translate_text(text)

    print("\n" + "=" * 40)
    print(f"Original:  {text}")
    print(f"Translated: {result}")
    print("=" * 40 + "\n")

    if len(sys.argv) == 1:
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()