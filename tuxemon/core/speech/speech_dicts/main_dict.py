from core.components.game_event import *


speech_dictionary = {}

def parse_speech(textKey, text):
    textKey_L = textKey.lower()
    if textKey_L in speech_dictionary:
        pygame.event.post(speech_dictionary[textKey_L](text))
