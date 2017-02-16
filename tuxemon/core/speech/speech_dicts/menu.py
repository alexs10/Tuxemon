from core.components.game_event import *
from main_dict import speech_dictionary

synonyms = ["open", "menu", "then you", "okay", "man you", "men you"]

def menu_event(speech_text):
    return pygame.event.Event(MENU_EVENT)


for key in synonyms:
    speech_dictionary[key] = menu_event
