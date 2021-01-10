import pyaudio
import wave
import speech_recognition as sr
import subprocess
from mlol.commands import say, Commander


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, "rb")
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )
    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()

    pa.terminate()


r = sr.Recognizer()


def initSpeech():
    print("Listening : ")
    play_audio("./note1.wav")
    with sr.Microphone() as source:
        say("Say something")
        audio = r.listen(source)
    play_audio("./note7.wav")
    command = ""
    try:
        say("trying to recognize")
        command = r.recognize_google(audio)
        say("your command was " + command)
    except:
        say("Couldnt understand you")


initSpeech()