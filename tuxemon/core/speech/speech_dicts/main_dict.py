from core.components.game_event import *


speech_dictionary = {}

def parse_speech(textKey, text):
    textKey_L = textKey.lower()
    words = textKey_L.split()
    for word in words:
        if word in speech_dictionary:
            print(word)
            pygame.event.post(speech_dictionary[word](text))
