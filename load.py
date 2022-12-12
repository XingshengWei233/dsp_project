import librosa

MUSIC = "For River.mp3"
y, sr = librosa.load(MUSIC, sr=44100)
print(y.shape)