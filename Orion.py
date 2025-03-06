import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Wait for few seconds...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        query = "None"
    return query