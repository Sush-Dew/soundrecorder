import sounddevice as sd 
from scipy.io.wavfile import write 

duration = 30.5 
fs = 48000
myrecording = sd.rec(int(duration * fs), samplerate = fs, channels=2)

sd.default.samplerate = fs
sd.default.channels = 2 


sd.wait()

write("recording.wav", fs , myrecording)