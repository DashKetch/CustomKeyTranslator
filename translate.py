import random
import string
from typing import Optional
from config import get_language_file_path
from validate import load_and_validate


class Translator:
    def __init__(self, lang_code: str):
        self.lang_code = lang_code
        self.mappings = {}
        self._load_resources()

    def _load_resources(self):
        """Internal method to load and validate the language file."""
        path = get_language_file_path(self.lang_code)
        data = load_and_validate(path)

        if data:
            self.mappings = data
            # Remove metadata key to keep only translations
            self.mappings.pop("language", None)
        else:
            print(f"Warning: Could not load language '{self.lang_code}'. No translations applied.")

    def _get_translation(self, word: str) -> str:
        """
        Looks up a single word.
        Handles randomization if the value is a list.
        Returns original word if key is missing.
        """
        # Normalize key for lookup (case-insensitive)
        key = word.lower()

        if key in self.mappings:
            val = self.mappings[key]
            if isinstance(val, list):
                return random.choice(val)
            return val

        return word

    def translate_text(self, text: str) -> str:
        """
        Splits text into words, translates known words, and reconstructs the sentence.
        Preserves basic punctuation attached to words.
        """
        if not self.mappings:
            return text

        translated_words = []
        words = text.split()

        for original_token in words:
            # Strip punctuation to find the clean word key
            clean_word = original_token.strip(string.punctuation)
            punctuation = original_token[len(clean_word):] if clean_word else original_token
            prefix = original_token[:original_token.find(clean_word)] if clean_word else ""

            # Translate the clean word
            if clean_word:
                translated_core = self._get_translation(clean_word)

                # Attempt to preserve capitalization
                if clean_word.istitle():
                    translated_core = translated_core.capitalize()
                elif clean_word.isupper():
                    translated_core = translated_core.upper()

                translated_words.append(f"{prefix}{translated_core}{punctuation}")
            else:
                # Handle edge cases (only punctuation)
                translated_words.append(original_token)

        return " ".join(translated_words)