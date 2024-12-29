import pyttsx3

engine = pyttsx3.init()

def speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()
