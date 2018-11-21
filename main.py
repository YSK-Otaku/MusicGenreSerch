import librosa

x, fs = librosa.load('test01.wav', sr=44100)
mfccs = librosa.feature.mfcc(x, sr=fs)
print(mfccs.shape)

