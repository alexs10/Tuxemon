from core.components.game_event import *
from main_dict import speech_dictionary

north_synonyms  = ["north"]
east_synonyms   = ["east"]
south_synonyms  = ["south", "now"]
west_synonyms   = ["west"]


def north_event(speech_text):
    return pygame.event.Event(NORTH_EVENT)

def east_event(speech_text):
    return pygame.event.Event(EAST_EVENT)

def south_event(speech_text):
    return pygame.event.Event(SOUTH_EVENT)

def west_event(speech_text):
    return pygame.event.Event(WEST_EVENT)



for key in north_synonyms:
    speech_dictionary[key] = north_event


for key in east_synonyms:
    speech_dictionary[key] = east_event


for key in south_synonyms:
    speech_dictionary[key] = south_event


for key in west_synonyms:
    speech_dictionary[key] = west_event
