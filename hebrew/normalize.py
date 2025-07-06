import argparse, os
from pydub import AudioSegment
from pydub.effects import normalize
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

os.makedirs(args.output, exist_ok=True)
files = [f for f in os.listdir(args.input) if f.endswith('.wav')]

for fname in tqdm(files, desc='Processing'):
    path = os.path.join(args.input, fname)
    audio = AudioSegment.from_wav(path)
    audio = audio.set_channels(1).set_frame_rate(22050).set_sample_width(2)
    normalized = normalize(audio)
    normalized.export(os.path.join(args.output, fname), format='wav')
