import threading
import time

import os
import json
from os.path import join, dirname
from core.components.game_event import *

from speech_dicts import *

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()



IBM_USERNAME = "af3a03ef-27b9-49a6-94c4-04260b99a4b4"
IBM_PASSWORD = "kKsCsPRFfWYq"

def speech_thread():
    while 1:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
            print("IBM Speech to Text thinks you said " + text)
            parse_speech(text)
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))
    return
