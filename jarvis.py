import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import datetime #pip install datetime
import os #pip install os
import webbrowser #pip install webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("My Master's name is Swastik and Swastik is a good boy")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Master!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon Master!")

    else:
        speak("Good Evening Master!")

    speak("I am Jarvis, your personal assistant made with the help of AI(Artificial Intelligence) Made by- Master Swastik. I can do many things for you just give me any task")

def takeCommand():
    # It takes microphone input from the user and give a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According wikipedia")
            #print(results)
            speak(results)

        elif 'open notepad' in query:
            speak("opening notepad")
            n = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(n)

        elif 'close notepad' in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open this pc' in query:
            speak("ok sir, opening this pc")
            tp = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\this pc"
            os.startfile(tp)

        elif 'open adobe photoshop' in query or 'open adobe photoshop express' in query:
            speak("opening adobe photoshop express")
            ap = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Extras\\Photoshoot\\adobe_photoshop_express.lnk"
            os.startfile(ap)
        
        elif 'open command' in query or 'open command prompt' in query or 'open cmd' in query:
            speak("opening command prompt")
            cp = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cp)

        elif 'close cmd' in query or 'close command' in query or'close command prompt' in query:
            speak("ok sir, closing Command Prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            wh = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Extras\\whatsapp-desktop.ink"
            os.startfile(wh)

        elif 'close whatsapp' in query:
            speak("ok sir, closing whatsapp")
            os.system("taskkill /f /im whatsapp.exe")

        elif 'open zoom' in query:
            speak("Opening zoom")
            z = "C:\\Users\\Lenovo\\AppData\\Roaming\\Zoom\\bin\\zoom.exe"
            os.startfile(z)

        elif 'close zoom' in query:
            speak("Ok Sir, closing zoom")
            os.system("taskkill /f /im zoom.exe")

        elif 'open spotify' in query:
            speak("opening spotify")
            spot = "C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\spotify.exe"
            os.startfile(spot)

        elif 'close spotify' in query:
            speak("ok sir, closing spotify")
            os.system("teskkill /f /im soptify.exe")

        elif 'open racing game' in query:
            speak("opening Asphalt 9 Legends")
            a9l = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Gaming\\Asphalt 9 Legends.ink"
            os.startfile(a9l)

        elif 'open running game' in query:
            speak("opening Despicable Me Minion Rush")
            dmmr = "C:\\Users\Lenovo\\OneDrive\\Desktop\\Gaming\\Despicable Me Minion Rush.ink"
            os.startfile(dmmr)

        elif 'open among us' in query:
            speak("opening Among Us")
            au = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Gaming\\Among Us V.2020.9.9 By Naimchito\\Among Us.exe"
            os.startfile(au)

        elif 'open audacity' in query:
            speak("Opening Audacity")
            ac = "C:\\Program Files (x86)\\Audacity\\audacity.exe"
            os.startfile(ac)

        elif 'open utorrent' in query:
            speak("opening UTorrent Web")
            uw = "C:\\Users\\Lenovo\\AppData\\Roaming\\uTorrent Web\\utweb.exe"
            os.startfile(uw)

        elif 'open typing master' in query:
            speak("ing Typing Master 10")
            tm10 = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
            os.startfile(tm10)

        elif 'open wordpad' in query:
            speak("opening wordpad")
            wp = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wp)


        elif 'open tutorials' in query:
            speak("ok sir, I am opening my folder")
            jt = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Jarvis Tutorials" 
            os.startfile(jt)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.nl/")

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'play music' in query:
            speak("ok sir, Playing Music")
            music_dir = 'C:\\Users\\Lenovo\\Music'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'offline' in query:
            speak("ok sir, thank you for using me. Have a nice day")
            exit()