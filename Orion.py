import pyttsx3
import speech_recognition as sr
import datetime
import os

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

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")
    elif hour>=12 and hour<18:
        print("Good Afternoon Sir !")
        speak("Good Afternoon Sir !")    
    elif hour>=18 and hour<21:
        print("Good Evening Sir !")
        speak("Good Evening Sir !")
    else:
        print("Good Night Sir !")
        speak("Good Night Sir !")


if __name__ == "__main__": 
    wishings()
    query = commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")
    
    elif 'open Brave' in query:
        speak("Opening Brave Browser Sir...")
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")