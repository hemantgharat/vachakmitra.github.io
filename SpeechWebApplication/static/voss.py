from vosk import Model ,KaldiRecognizer
import pyaudio

result=[]
ap=[]
model=Model("./model/vosk-model-en-in-0.5")
recognizer=KaldiRecognizer(model,16000)

mic=pyaudio.PyAudio()
voice=mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=1024)
voice.start_stream()
print(type(voice))
print('Recording....')
while True:
    data=voice.read(1024)
    print(type(data))
    if recognizer.AcceptWaveform(data):
        temp=(recognizer.Result()[14:-3])
        print(temp)
