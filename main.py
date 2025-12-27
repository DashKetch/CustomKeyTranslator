import sys
import config
from cli import parse_args
from translate import Translator


def main():
    # Ensure folder exists before doing anything else
    created_new = config.ensure_languages_setup()
    if created_new:
        print(f"--- Notice: Created new 'languages' folder at {config.LANG_DIR} ---")

    if len(sys.argv) > 1:
        args = parse_args()
        lang = args.lang
        text = args.text
    else:
        print("--- Custom Language Translator ---")
        available = config.list_available_languages()
        if available:
            print(f"Available languages: {', '.join(available)}")

        lang = input("Enter target language: ").strip()
        text = input("Enter text to translate: ").strip()

    translator = Translator(lang)
    result = translator.translate_text(text)

    print("\n" + "=" * 40)
    print(f"Translated: {result}")
    print("=" * 40 + "\n")

    if len(sys.argv) == 1:
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()