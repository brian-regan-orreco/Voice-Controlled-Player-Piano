#listen.py
#captures input and computes intent

import speech_recognition as sr
from time import sleep

launchPhrase = "piano"
keyWords = ["stop", "pause", "exit", "play"]

#get audio input
def getSpeech():
    r = sr.Recognizer()
    m = sr.Microphone()
    speech = ""
    print("Calibrating for background noise...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    print("Got it! Now to recognize it...")
    try:
        # recognize speech using Google Speech Recognition
        speech = r.recognize_google(audio).lower()
        print("You said {}".format(speech))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    return speech

#identify the intent of a command
def getIntent(speech, keyWords = keyWords):
        print("speech is:", speech)
        if speech is not "" and launchPhrase in speech:
            for intent in keyWords:
                #print("checking", intent)
                if intent in speech:
                    print("intent found:", intent)
                    return intent
        return None

#returns 2tuple (artist, [words, in , song, title])
#or (artist/song, None) if just one given
def getArtistSong(value):
    value = value.lower()
    value = value.split("play ")[-1]
    if value in ["all", "everything", "music", "some music"]:
        return "all"
    value = value.split("some ")[-1]
    value = value.replace(" please", "")
    value = value.split(" by ")
    try:
        artist = value[1]
        song = value[0].split(" ")
        return (artist, song)
    except:
        return(value[0], None)