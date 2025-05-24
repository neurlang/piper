import argparse
import json


def raw_phoneme_id_map(path):
    base = {'_': 0, '^': 1, '$': 2, ' ': 3}  # pad, bos, eos, whitespace
    phoneme_map = dict(base)  # copy base dict
    next_id = max(base.values()) + 1

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            phonemes = data.get('phonemes', [])
            for p in phonemes:
                if p not in phoneme_map:
                    phoneme_map[p] = next_id
                    next_id += 1

    return phoneme_map


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build phoneme to ID map from dataset")
    parser.add_argument('jsonl_path', type=str, help='Path to input JSONL file')
    args = parser.parse_args()

    phoneme_id_map = raw_phoneme_id_map(args.jsonl_path)
    print(json.dumps(phoneme_id_map, ensure_ascii=False))
