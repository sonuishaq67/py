import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
import json
from bs4 import BeautifulSoup as soup
import random
from time import strftime


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command


def sofiaResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("echo "+line)


sofiaResponse('Hi User, I am Sophia and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')


def assistant(command):
     if 'shutdown now' in command:
        os.system("shutdown now")


while True:
    assistant(myCommand())