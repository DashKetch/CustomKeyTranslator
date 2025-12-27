import sys
import os
from pathlib import Path


def get_base_path():
    """
    Determines the directory where the executable or script is located.
    """
    if getattr(sys, 'frozen', False):
        # Path to the folder where the .exe lives
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent


BASE_DIR = get_base_path()
LANG_DIR = BASE_DIR / "languages"


def ensure_languages_setup():
    """
    Creates the languages folder and a high-quality starter template if missing.
    """
    if not LANG_DIR.exists():
        LANG_DIR.mkdir(parents=True, exist_ok=True)

        example_file = LANG_DIR / "es.json"
        if not example_file.exists():
            import json
            # A more complete dictionary to test randomization and context
            example_data = {
                "language": "es",
                "hello": ["hola", "buenos días", "buena mañana", "buenas tardes"],
                "hi": ["hombre", "chulo", "tío"],
                "goodbye": ["adiós", "hasta luego", "hasta siempre", "chau", "despedida"],
                "see you later": ["te veré pronto", "mejoré", "te vemos más tarde"],
                "see you soon": ["te veré en poco tiempo", "estoy cerca de ti"],
                "hello how are you": ["¿cómo estás?", "¿qué tal?", "¿cómo vas?"],
                "thank you": ["gracias", "de nada", "por favor"],
                "excuse me": ["¡disculpa!", "perdón", "¿puedo pedir algo?"],
                "one": ["uno", "un solo"],
                "two": ["dos", "dos veces"],
                "three": ["tres", "tres veces"],
                "four": ["cuatro", "cuatro veces"],
                "five": ["cinco", "cince"],
                "six": ["seis", "seis veces"],
                "seven": ["siete", "seis veces"],
                "eight": ["ocho", "ocho veces"],
                "nine": ["nueve", "nueve veces"],
                "ten": ["diez", "diez veces"],
                "red": ["rojo", "rojo brillante"],
                "blue": ["azul", "azul claro"],
                "green": ["verde", "verde intenso"],
                "yellow": ["amarillo", "amarillo brillante"],
                "orange": ["naranja", "naranja brillante"],
                "purple": ["púrpura", "púrpura oscuro"],
                "pink": ["rosa", "rosa pastel"],
                "brown": ["marrón", "marrón claro"],
                "gray": ["gris", "gris claro"],
                "black": ["negro", "negro oscuro"],
                "white": ["blanco", "blanco intenso"],
                "apple": ["manzana", "manzana roja"],
                "banana": ["plátano", "plátano amarillo"],
                "cherry": ["cerro", "cerro rojo"],
                "date": ["datta", "datta madera"],
                "elderberry": ["rambla", "rambla de frutas"],
                "fig": ["higos", "higos verdes"],
                "grape": ["uva", "uva azul"],
                "honeydew": ["melón de miel", "melón de miel verde"],
                "ice cream": ["helado", "helado con frutas"],
                "jackfruit": ["piña", "piña tropical"]
            }
            with open(example_file, 'w', encoding='utf-8') as f:
                json.dump(example_data, f, indent=2, ensure_ascii=False)
        return True
    return False


def list_available_languages():
    if not LANG_DIR.exists():
        return []
    return [f.stem for f in LANG_DIR.glob("*.json")]


def get_language_file_path(lang_code: str) -> Path:
    return LANG_DIR / f"{lang_code}.json"


DEFAULT_LANG = "es"
