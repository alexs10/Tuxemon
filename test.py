import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()



IBM_USERNAME = "af3a03ef-27b9-49a6-94c4-04260b99a4b4"
IBM_PASSWORD = "kKsCsPRFfWYq"


while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Sphinx
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))
