"""
uv venv
uv pip install piper_phonemize
uv run hebrew/create_test.py > etc/test_sentences/test_he.jsonl 
"""
import json
import piper_phonemize

phonemes = [
    "ʃalˈom olˈam! mˈa korˈe?",
    "bˈo teʁˈed, toχˈal ktsˈat tˈeʁed. ʔˈejze tχinˈa! jihjˈe tχˈina tovˈa! bˈo niʃtˈe bˈiʁa beʔˈiʁ habiʁˈa! hˈu pitˈa ʔotˈi leʔeχˈol pˈita ʃawˈaʁma!"
]

for p in phonemes:
    p = list(p)
    ids =  piper_phonemize.phoneme_ids_espeak(p)
    print(json.dumps({"text": "".join(p), "phonemes": p, "phoneme_ids": ids}, ensure_ascii=False), end='\n')

