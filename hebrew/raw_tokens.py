import argparse
import random
import os

# Cleaned token set for Piper
piper_256_tokens = ' !"#$\'(),-.0123456789:;?^_abcdefhijklmnopqrstuvwxyzæçðøħŋœǀǁǂǃɐɑɒɓɔɕɖɗɘəɚɛɜɞɟɠɡɢɣɤɥɦɧɨɪɫɬɭɮɯɰɱɲɳɴɵɶɸɹɺɻɽɾʀʁʂʃʄʈʉʊʋʌʍʎʏʐʑʒʔʕʘʙʛʜʝʟʡʢʰʲˈˌːˑ˞ˤ̧̩̪̯̺̻̃βεθχᵻ↑↓ⱱ'
piper_256_tokens = ''.join(i for i in piper_256_tokens if i not in ' $^_') # remove special tokens

def is_hebrew_char(c):
    return '\u05b0' <= c <= '\u05ea'

def map_hebrew_to_random_tokens(input_path, output_path):
    hebrew_chars = set()
    lines = []

    with open(input_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            lines.append(line.strip())
            parts = line.strip().split('|')
            if len(parts) == 2:
                phonemes = parts[1]
                for ch in phonemes:
                    if is_hebrew_char(ch):  # skip spaces/newlines
                        hebrew_chars.add(ch)

    # Map each unique Hebrew char to a unique random Piper token
    if len(hebrew_chars) > len(piper_256_tokens):
        raise ValueError("Not enough Piper tokens to cover all Hebrew characters.")

    mapping = dict(zip(hebrew_chars, random.sample(piper_256_tokens, len(hebrew_chars))))

    print("Mapping:", mapping)  # Optional: Show for debugging

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            parts = line.split('|')
            if len(parts) == 2:
                file_id, phonemes = parts
                mapped = ''.join(mapping.get(ch, ch) for ch in phonemes)
                outfile.write(f"{file_id}|{mapped}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map Hebrew phonemes to Piper-compatible random tokens.")
    parser.add_argument("input", help="Path to the input metadata.csv file with Hebrew characters.")
    parser.add_argument("output", help="Path to the output file with Piper-compatible tokens.")
    args = parser.parse_args()

    map_hebrew_to_random_tokens(args.input, args.output)
