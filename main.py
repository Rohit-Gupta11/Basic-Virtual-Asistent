import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour = datetime.datetime.now().hour
    if hour in range(0,12):
        speak("Good Morning")
    elif hour in range(12,18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am rubic.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.........")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        print("say that again please.....")
        return "None"
    return query

if __name__ == "__main__":
    wish()

    while True:
        query = takeCommand().lower()

        # wikipedia logic
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        # for opening website in browser
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")