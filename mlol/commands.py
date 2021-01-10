import os, subprocess


def say(text):
    subprocess.call(f"say {text}", shell=True)


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "sure", "si", "do it", "yeah", "confirm"]
        self.cancel = ["no", "nope", "negative", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            say("my name is bruh")
