"""
uv venv
uv pip install piper_phonemize mishkal
uv run hebrew/create_test.py > etc/test_sentences/test_he.jsonl 
"""
# import mishkal
import json
import piper_phonemize

phonemes = [
    "ʃalˈom olˈam! mˈa koʁˈe?",
    "bˈo teʁˈed, toχˈal ktsˈat tˈeʁed. ʔˈejze tχinˈa! jihjˈe tχˈina tovˈa! bˈo niʃtˈe bˈiʁa beʔˈiʁ habiʁˈa! hˈu pitˈa ʔotˈi leʔeχˈol pˈita ʃawˈaʁma!",
    "sˈimu lˈev, nosʔˈim jekaʁˈim. haʁakˈevet letˈel ʔavˈiv meʁkˈaz tikanˈes leʁatsˈif mispˈaʁ ʃalˈoʃ beʔˈod mispˈaʁ dakˈot. ʔˈana hitʁaχakˈu miktsˈe haʁatsˈif vehamtˈinu meʔaχoʁˈej hakˈav hatsahˈov."
]

for p in phonemes:
    p = list(p)
    ids =  piper_phonemize.phoneme_ids_espeak(p)
    print(json.dumps({"text": "".join(p), "phonemes": p, "phoneme_ids": ids}, ensure_ascii=False), end='\n')

