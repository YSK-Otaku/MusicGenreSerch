import librosa
import glob

def getmfcc(path):
    x, fs = librosa.load(path, sr=44100)
    mfccs = librosa.feature.mfcc(x, sr=fs)
    print(mfccs.shape,path)

file = glob.glob('*.wav')
for f in file:
 getmfcc(f)

