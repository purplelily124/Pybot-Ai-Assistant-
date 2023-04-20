import subprocess
import pyttsx4
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
from ecapture import ecapture as ec
engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Maam !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Maam !")  
  
    else:
        speak("Good Evening Maam !") 
  
    assname =("Pybot 1 point o")
    speak("I am your Assistant")
    speak(assname)
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5, phrase_time_limit=5)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
     
    while True:
         
        query = takeCommand().lower()
         
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play spotify' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "https://open.spotify.com/track/1juJ3mwsFerctbngtK42G4?si=08d98654c55443d7"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'the time' in query:
            now=datetime.now()
            strTime = now.strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                  
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Pybot Camera ", "img.png")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
