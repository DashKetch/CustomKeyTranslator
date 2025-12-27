# Custom Language Translator

A modular, Python-based translator that uses local JSON files to map words from a base language (English) to a target language. It features randomization for synonymous words, strict validation of language files, and a simple CLI.

## Project Structure

- **languages/**: Contains JSON files defining translations.
- **config.py**: Central configuration for paths and defaults.
- **validate.py**: Ensures JSON files are syntactically correct and follow the required schema.
- **translate.py**: Logic for loading resources and processing text.
- **main.py**: The entry point for the application.

## Setup

1. Ensure you have Python 3 installed.
2. No external libraries are required (uses standard library only).

## Usage

Run the `main.py` file from the terminal.

### Basic Usage
```bash
python main.py --lang es --text "Hello world"
```

### Using a different language file (e.g., Pirate)
```Bash
python main.py --lang pirate --text "Hello friend, do you have money?"
```
### Adding New Languages
1. Create a new .json file in the languages/ directory (e.g., fr.json).

2. Follow this structure:

```JSON
{
  "language": "fr",
  "hello": "bonjour",
  "bye": ["au revoir", "adieu"]
}
```

3. Use the filename as the --lang argument (e.g., --lang fr).