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
                "hello": "hola",
                "hi": ["hola", "buenas", "qué tal"],
                "goodbye": ["adiós", "hasta luego", "chao"],
                "see you later": ["te veo luego", "hasta más tarde", "nos vemos"],
                "see you soon": ["hasta pronto", "nos vemos pronto", "te veré pronto"],
                "thanks": ["gracias", "muchas gracias", "mil gracias"],
                "please": ["por favor", "porfa", "se lo ruego"],
                "sorry": ["lo siento", "perdón", "disculpa"],
                "friend": ["amigo", "colega", "compañero", "pana"],
                "family": ["familia", "parientes", "linaje"],
                "mother": ["madre", "mamá", "mami"],
                "father": ["padre", "papá", "papi"],
                "water": ["agua", "h2o", "líquido"],
                "food": ["comida", "alimento", "nutrición"],
                "dog": ["perro", "can", "perrito", "cachorro"],
                "cat": ["gato", "felino", "gatito", "michi"],
                "bird": ["pájaro", "ave", "pajarraco"],
                "fish": ["pez", "pescado", "criatura marina"],
                "sun": ["sol", "astro rey", "luz solar"],
                "moon": ["luna", "satélite", "astro nocturno"],
                "star": ["estrella", "astro", "lucero"],
                "rain": ["lluvia", "precipitación", "aguacero", "chubasco"],
                "wind": ["viento", "brisa", "aire", "vendaval"],
                "hot": ["caliente", "caluroso", "ardiente"],
                "cold": ["frío", "gélido", "helado"],
                "happy": ["feliz", "alegre", "contento", "radiante"],
                "sad": ["triste", "deprimido", "apenado", "melancólico"],
                "big": ["grande", "enorme", "gigante", "vasto"],
                "small": ["pequeño", "chico", "diminuto", "breve"],
                "fast": ["rápido", "veloz", "pronto", "acelerado"],
                "slow": ["lento", "pausado", "despacio"],
                "book": ["libro", "ejemplar", "tomo", "volumen"],
                "school": ["escuela", "colegio", "instituto", "academia"],
                "city": ["ciudad", "urbe", "metrópolis"],
                "house": ["casa", "hogar", "vivienda", "residencia"],
                "eat": ["comer", "ingerir", "alimentarse", "nutrirse"],
                "drink": ["beber", "tomar", "sorber", "hidratarse"],
                "sleep": ["dormir", "pernoctar", "descansar", "reposar"],
                "run": ["correr", "trotar", "escapar", "apresurarse"],
                "walk": ["caminar", "andar", "pasear", "marchar"],
                "work": ["trabajar", "laborar", "faenar", "currar"],
                "love": ["amor", "querer", "afecto", "cariño"]
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
