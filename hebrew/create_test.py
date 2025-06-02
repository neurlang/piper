"""

uv venv
uv pip install piper_phonemize mishkal phonemizer-fork espeakng-loader
uv run hebrew/create_test.py > etc/test_sentences/test_he.jsonl 

wget https://huggingface.co/thewh1teagle/phonikud-tts-checkpoints/resolve/main/model.config.json
uv run hebrew/create_test.py model.config.json
"""
# import mishkal
import json
# import piper_phonemize
# from phonemizer.backend.espeak.wrapper import EspeakWrapper
# import phonemizer
# import espeakng_loader
import sys
from pathlib import Path

# EspeakWrapper.set_library(espeakng_loader.get_library_path())
# EspeakWrapper.set_data_path(espeakng_loader.get_data_path())



phonemes = [
    # "ʃalˈom olˈam! mˈa koʁˈe?",
    "sˈimu lev nosʔˈim jekaʁˈim. haʁakˈevet letel ʔavˈiv meʁkˈaz tikanˈes leʁatsˈif mispˈaʁ ʃalˈoʃ beʔˈod mispˈaʁ dakˈot. ʔˈana hitʁaχakˈu miktsˈe haʁatsˈif vehamtˈinu meʔaχoʁˈej hakˈav hatsahˈov, todˈa!",
    # "mˈa zˈe mˈa atˈa zˈe atˈa mˈa atˈa omˈer",
    # "bˈo teʁˈed, toχˈal ktsˈat tˈeʁed. ʔˈejze tχinˈa! jihjˈe tχˈina tovˈa! bˈo niʃtˈe bˈiʁa beʔˈiʁ habiʁˈa! hˈu pitˈa ʔotˈi leʔeχˈol pˈita ʃawˈaʁma!",
    # "uṽn, bvɪaʊɾ! ɟ̃8ɥǀ ɟr:ħ8 8ʉucðɶ ɶʊɭŗðɞ ɶʉɥǀ ʜʊ8vcðɚ?"
    # "ɬɳɠ ɬɤˌɛtɠ vʏχsɳɑɠ mʎːʏɛʛɻ ɨɤm ˈɛɥʛᵻʎvɥbtɠ, ɬtˌ ʄɤʛɻɥʟɛʎɨʏχˌʎɑʏ ʛɻtm ʛɻɳɑnɛʏɛɑ ʄʎɬɤǃɥmɳɑɠ,"
    # phonemizer.phonemize('Just kicking back with some good music, letting the vibes do their thing.')
]

def get_ids(phonemes: list[str]) -> list[int]:
    _BOS = "^"
    _EOS = "$"
    _PAD = "_"
    with open(sys.argv[1]) as fp:
        map_data = json.load(fp)
        map_data = map_data['phoneme_id_map']
    ids = [map_data[_BOS][0]]
    for p in phonemes:
        if p in map_data:
            ids.extend(map_data[p])
            ids.extend(map_data[_PAD])
    ids.extend(map_data[_EOS])
    return ids

for p in phonemes:
    p = list(p)
    # ids =  piper_phonemize.phoneme_ids_espeak(p)
    ids =  get_ids(p)
    data = json.dumps({"text": "".join(p), "phonemes": p, "phoneme_ids": ids}, ensure_ascii=False) + '\n'
    print(data)
    with open(Path(__file__).parent / '../etc/test_sentences/test_he.jsonl', 'w', encoding='utf-8') as fp:
        fp.write(data)




