import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Convert phonemes.json to pipe-separated file")
    parser.add_argument("json_path", type=Path, help="Path to input phonemes.json")
    parser.add_argument("output_path", type=Path, help="Path to output file")
    args = parser.parse_args()

    data = json.load(args.json_path.open(encoding="utf-8"))

    # Prepare lines: file_id|phonemes (joining phonemes list if needed)
    lines = []
    for file_id, phonemes in data.items():
        if isinstance(phonemes, list):
            phonemes = " ".join(phonemes)
        lines.append(f"{file_id}|{phonemes}")

    content = "\n".join(lines)

    args.output_path.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
