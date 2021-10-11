# Importing all necessary libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyjokes
import pywhatkit

# Below I have defined the speak function which converts text to speach using the pytttsx3 module
def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    print(string)
    engine.runAndWait()

# The function that I have defined below is to wish me according to the time using the datetime module
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, your virtual voice assistant. How may I help you?")

# The function that I have defined below is to convert speech to text using the speech recognition module
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold= 1/2
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}")

    except:
        pass

    return query

# The below conditions are to wish me once when I run the code
# and loop through the take command function and all conditions that are below the while true condition
if __name__ == "__main__":
    wishMe()
    while True:
        text = takeCommand().lower()
        # The condition below checks if the word wikipedia is in the text that we have spoken
        # And if it is there in the text the code searches what we have spoken in wikipedia
        if 'wikipedia' in text:
            try:
                text = text.replace("wikipedia", "")
                results = wikipedia.summary(text, sentences=3)
                speak("According to Wikipedia")
                speak(results)
            # if there is no article in wikipedia about what you have spoken,
            # instead of throwing an error it searches what you have told in google
            # and gives you the answer accordingly
            except:
                try:
                    text = text.replace("wikipedia", "")
                    webbrowser.open(f"https://www.google.com/search?q={text}")
                # and if at all there are no results in google about what you have spoken
                # instead of opening google with the error it says "Hmm... I don't know that"
                except:
                    speak("Hmm... I don't know that")
        # if the user mentions search google in the text then the virtual assistant searches your query in google
        elif 'search google' in text:
            speak("ok, what do I search?")
            search = takeCommand()
            speak("ok, here's what I found")
            webbrowser.open(f"https://www.google.com/search?q={search}")

        # and if the user mentions search youtube in the text
        # then the virtual assistant searches your query in youtube
        elif "search youtube" in text:
            speak("Sure, what do you want me to search?")
            query1 = takeCommand().lower()
            speak("okay, here's what I found")
            webbrowser.open(f"https://www.youtube.com/search?q={query1}")

        # The below conditions are for opening folders
        # first, the virtual assistant will ask you which file you want to open
        # and it will try to see if any such folder is there in your desktop, Downloads or Documents (You cantweek the code as per your requirement to put your foldre's names)
        # and if it cannot find the folder that you have requested then it will ask you to type the name of the file that you want to open
        elif 'open a file' in text:
            speak("sure, which file do you want me to open? Please say the name of the file with its extention")
            query = takeCommand()
            try:
                os.startfile(f"C:\\Users\\apex\\Documents\\{query}")
            except:
                try:
                    os.startfile(f"C:\\Users\\apex\\Downloads\\{query}")
                except:
                    try:
                        os.startfile(f"C:\\Users\\apex\\Desktop\\{query}")
                    except:
                        speak("sorry, there must have been an error in recognizing your voice. Please type the name of the file you want to open below")
                        file_name = input("please type the file name here with its extension: ")
                        try:
                            os.startfile(f"C:\\Users\\apex\\Documents\\{file_name}")
                        except:
                            try:
                                os.startfile(f"C:\\Users\\apex\\Downloads\\{file_name}")
                            except:
                                try:
                                    os.startfile(f"C:\\Users\\apex\\Desktop\\{file_name}")
                                except:
                                    speak("Sorry, There is no such file as your request in Downloads, Desktop or Documents, You can try openning the file manually.")

        # The above condition opens YouTube
        # Using the webbrowser module
        elif 'open youtube' in text:
                speak("opening youtube")
                webbrowser.open("youtube.com")

        # The above condition opens google
        # Using the webbrowser module
        elif 'open google' in text:
            speak("opening google chrome")
            webbrowser.open("google.com")

        # The above condition opens your Stackoverflow
        # Using the webbrowser module
        elif 'open stack overflow' in text:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        # The above condition opens your Github when you ask it to
        # Using the webbrowser module
        elif 'open github' in text:
            speak("opening github")
            webbrowser.open("github.com")

        # The below condition opens Krunker (which is an online multi-player game that you can play on your browser without downloading ) when you ask it to
        # Using the webbrowser module
        elif 'open krunker' in text:
            speak("opening krunker")
            webbrowser.open("krunker.io")

        # The below condition opens classic minecraft ( not the real one just a clone of the actual one that you can play on your browser for free ) when you ask it to
        # Using the webbrowser module
        elif 'open minecraft' in text:
            speak("opening minecraft")
            webbrowser.open("classic.minecraft.net")

        # The below condition opens Tanki online (which is an online multi-player game that you can play on your browser without downloading ) when you ask it to
        # Using the webbrowser module
        elif 'open tanki online' in text:
            speak("opening tanki online")
            webbrowser.open("tankionline.com")

        # The below condition opens your gmail when you ask it to
        # Using the webbrowser module
        elif 'open my gmail' in text:
            speak("opening your gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        # The below condition tell you the present time when you say time when you are speaking
        # Using the dateTime module
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {strTime}")

        # When you mention play the below condition plays the related video on youtube
        # using the pywhatkit module
        elif 'play' in text:
            text = text.replace("play", "")
            speak("Okay, playing your request")
            pywhatkit.playonyt(text)

        # The next few below conditions are to answer some commonly asked questions to a virtual assistant
        # That are who made you or What is your name?
        elif 'your name' in text:
            speak("my name is JARVIS")

        elif 'your good name' in text:
            speak("my name is JARVIS")

        elif 'what can you do' in text:
            speak("I am Jarvis, your virtual assistant, I can open files, perform google or wikipedia searches, tell you jokes, open your favourite websites, etc.")

        elif 'your creator' in text:
            speak("I was created by Gabriel Obed")

        elif 'made you' in text:
            speak("I was created by Gabriel Obed")

        elif 'created you' in text:
            speak("I was created by Gabriel Obed")

        # The below condition tells you a joke when you ask it to using the pyjoke module
        elif 'joke' in text:
            joke = pyjokes.get_joke()
            speak(joke)

        # The below condition stop debuging/running the code when you say 'quit'
        elif 'quit' in text:
            sys.exit()

        # The below codition is to google or wikipedia search your query without you having to mention wikipedi or google search
        else:
            try:
                results = wikipedia.summary(text, sentences=3)
                speak("According to Wikipedia")
                speak(results)
            except:
                try:
                    webbrowser.open(f"https://www.google.com/search?q={text}")
                except:
                    speak("hmm... I don't know that")