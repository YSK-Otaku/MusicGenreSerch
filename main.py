import librosa
import glob

def getmfcc(path):
    x, fs = librosa.load(path, sr=44100)
    mfccs = librosa.feature.mfcc(x, sr=fs)
    print(mfccs[0])

def getBPM(path):
    x, fs = librosa.load(path, sr=44100)
    y = librosa.onset.onset_strength(x, fs)
    bpm = librosa.beat.tempo(onset_envelope=y, sr=fs)
    print(bpm)

file = glob.glob('*.wav')
for f in file:
    getBPM(f)

