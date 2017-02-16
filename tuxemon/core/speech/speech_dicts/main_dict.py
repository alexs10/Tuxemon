from core.components.game_event import *


speech_dictionary = {}

def parse_speech(textKey, text):
    if textKey in speech_dictionary:
        pygame.event.post(speech_dictionary[textKey](text))
