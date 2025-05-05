"""
uv venv
uv pip install piper_phonemize mishkal phonemizer-fork espeakng-loader
uv run hebrew/create_test.py > etc/test_sentences/test_he.jsonl 
"""
# import mishkal
import json
import piper_phonemize

from phonemizer.backend.espeak.wrapper import EspeakWrapper
import phonemizer
import espeakng_loader

EspeakWrapper.set_library(espeakng_loader.get_library_path())
EspeakWrapper.set_data_path(espeakng_loader.get_data_path())



phonemes = [
    "ʃalˈom olˈam! mˈa koʁˈe?",
    "bˈo teʁˈed, toχˈal ktsˈat tˈeʁed. ʔˈejze tχinˈa! jihjˈe tχˈina tovˈa! bˈo niʃtˈe bˈiʁa beʔˈiʁ habiʁˈa! hˈu pitˈa ʔotˈi leʔeχˈol pˈita ʃawˈaʁma!",
    "sˈimu lˈev nosʔˈim jekaʁˈim. haʁakˈevet letel ʔavˈiv meʁkˈaz tikanˈes leʁatsˈif mispˈaʁ ʃalˈoʃ beʔˈod mispˈaʁ dakˈot. ʔˈana hitʁaχakˈu miktsˈe haʁatsˈif vehamtˈinu meʔaχoʁˈej hakˈav hatsahˈov.",
    phonemizer.phonemize('Just kicking back with some good music, letting the vibes do their thing.')
]

for p in phonemes:
    p = list(p)
    ids =  piper_phonemize.phoneme_ids_espeak(p)
    print(json.dumps({"text": "".join(p), "phonemes": p, "phoneme_ids": ids}, ensure_ascii=False), end='\n')



