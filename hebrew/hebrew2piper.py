import json
import argparse

def is_hebrew_char(c):
    return '\u05b0' <= c <= '\u05ea'

def map_sentence(sentence: str, mapping: dict) -> str:
    return ''.join(mapping.get(c, c) for c in sentence)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Hebrew sentence to mapped Piper tokens.")
    parser.add_argument("mapping", help="Path to the mapping JSON file (hebrew2piper.json)")
    parser.add_argument("sentence", help="The Hebrew sentence to convert")

    args = parser.parse_args()

    # Load mapping
    with open(args.mapping, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    converted = map_sentence(args.sentence, mapping)
    print(converted)
