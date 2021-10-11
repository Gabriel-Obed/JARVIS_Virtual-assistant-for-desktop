import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyjokes
import pywhatkit

def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    print(string)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, your virtual voice assistant. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold= 1/2
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        text = takeCommand().lower()
        if 'wikipedia' in text:
            try:
                text = text.replace("wikipedia", "")
                results = wikipedia.summary(text, sentences=3)
                speak("According to Wikipedia")
                speak(results)
            except:
                    text = text.replace("wikipedia", "")
                    webbrowser.open(f"https://www.google.com/search?q={text}")

        elif 'search google' in text:
            speak("ok, what do I search?")
            search = takeCommand()
            speak("ok, here's what I found")
            webbrowser.open(f"https://www.google.com/search?q={search}")

        elif "search youtube" in text:
            speak("Sure, what do you want me to search?")
            query1 = takeCommand().lower()
            speak("okay, here's what I found")
            webbrowser.open(f"https://www.youtube.com/search?q={query1}")

        elif 'open a file' in text:
            speak("sure, which file do you want me to open? Please say the name of the file with its extention")
            query = takeCommand()
            try:
                os.startfile(f"C:\\Users\\apex\\Documents\\AI portfolio pdf.pdf")
            except:
                try:
                    os.startfile(f"C:\\Users\\apex\\Downloads{query}")
                except:
                    try:
                        os.startfile(f"C:\\Users\\apex\\Desktop{query}")
                    except:
                        speak("sorry, there must have been an error in recognizing your voice. Please type the name of the file you want to open below")
                        file_name = input("please type the file name here with its extension: ")
                        try:
                            os.startfile(f"C:\\Users\\apex\\Documents{file_name}")
                        except:
                            try:
                                os.startfile(f"C:\\Users\\apex\\Downloads{file_name}")
                            except:
                                try:
                                    os.startfile(f"C:\\Users\\apex\\Desktop{file_name}")
                                except:
                                    speak("Sorry, There is no such file as ou request in Downloads, Desktop or Documents, You can try openning the file manually.")

        elif 'open youtube' in text:
                speak("opening youtube")
                webbrowser.open("youtube.com")

        elif 'open google' in text:
            speak("opening google chrome")
            webbrowser.open("google.com")

        elif 'open stack overflow' in text:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in text:
            speak("opening github")
            webbrowser.open("github.com")

        elif 'open krunker' in text:
            speak("opening krunker")
            webbrowser.open("krunker.io")

        elif 'open minecraft' in text:
            speak("opening minecraft")
            webbrowser.open("classic.minecraft.net")

        elif 'open tanki online' in text:
            speak("opening tanki online")
            webbrowser.open("tankionline.com")

        elif 'open my gmail' in text:
            speak("opening your gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {strTime}")

        elif 'play' in text:
            text = text.replace("play", "")
            speak("Okay, playing your request")
            pywhatkit.playonyt(text)

        elif 'your name' in text:
            speak("my name is JARVIS")

        elif 'your good name' in text:
            speak("my name is JARVIS")

        elif 'what can you do' in text:
            speak("I am Jarvis, your virtual assitant, I can ")

        elif 'your creator' in text:
            speak("I was created by Gabriel Obed")

        elif 'made you' in text:
            speak("I was created by Gabriel Obed")

        elif 'created you' in text:
            speak("I was created by Gabriel Obed")

        elif 'joke' in text:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'quit' in text:
            sys.exit()

        else:
            try:
                results = wikipedia.summary(text, sentences=3)
                speak("According to Wikipedia")
                speak(results)
            except:
                if 'none' not in text:
                    try:
                        webbrowser.open(f"https://www.google.com/search?q={text}")
                    except:
                        speak("hmm... I don't know that")