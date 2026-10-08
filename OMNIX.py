import pyttsx3 # audio to text
import edge_tts 
import speech_recognition as sr # audio taker
import webbrowser # opening website
import time
import musicc   # importing musicc.py
import subprocess  # app opening
import appath      # importing appath.py
import os





def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def input():
     
     with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source) #timeout --> agar tu 2 sec kuch bola nhi to ye code crash ho jayega.
                global word1                                            #phrase_time_linit --> tu sirf 1 sec hi bol payega, jyada nhi
                word1 = recognizer.recognize_google(audio)

def command(word1):
    try:
        brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        webbrowser.register(
                'brave',
                None,
                webbrowser.BackgroundBrowser(brave)
                )
        if("open setting" in word1.lower()):
            speak("opening Sir")
            os.system("start ms-settings:")

        elif("open camera" in word1.lower()):
            speak("opening Sir")
            os.system("start microsoft.windows.camera:")

        elif("open war robot" in word1.lower()):
                speak("opening Sir")
                os.startfile("steam://rungameid/767560")

        elif("open google" in word1.lower()):
             speak("opening Sir")
             webbrowser.open("https://www.google.com/")

        elif("open youtube" in word1.lower()):
             speak("opening Sir")
             webbrowser.get('brave').open("https://www.youtube.com/")

        elif("open whatsApp" in word1.lower()):
            speak("opening Sir")
            webbrowser.open("https://web.whatsapp.com/")

        elif("open my linkedin profile" in word1.lower()):
            speak("opening Sir")
            webbrowser.open("https://www.linkedin.com/in/om-kale-ab5688374/")

        elif("open chat gpt" in word1.lower()):
            speak("opening Sir")
            webbrowser.open("https://www.chatgpt.com/")

        elif(word1.lower().startswith("play")):
            try:
                if(len(word1)>5):
                    song = word1.lower().split(" ")[1]
                    print(song)
                    speak(f"playing {song} music sir")
                    songlink = musicc.music[song]
                    if songlink:
                        webbrowser.get('brave').open(songlink)
                    else:
                        speak(f"sorry sir, {song} is not saved in my music list")
                else:
                    speak("sir, please tell the name of the song")
            except sr.UnknownValueError:
                    print("error ")

        elif(word1.lower().startswith("open")):
            try:
                if(len(word1)>5):
                    app = word1.lower().split(" ")[1]
                    print(app)
                    speak(f"opening {app} app sir")
                    apppath = appath.appp[app]
                    print(apppath)
                    subprocess.Popen(apppath)
                else:
                    speak("sir, please tell the name of the app")
            except sr.UnknownValueError:
                    print("error ")

    except sr.UnknownValueError:
        print("error ")




recognizer = sr.Recognizer()

if __name__ == "__main__":
    speak("Initializing Omnix.... ") 
    while True:
        

        print("recoding")
        # speak("yes")  
        try:
            input()
            # with sr.Microphone() as source:
            #             print("Listening...")
            #             audio = recognizer.listen(source, phrase_time_limit=1.5)
            #             #timeout --> agar tu 2 sec kuch bola nhi to ye code crash ho jayega.
            #             #phrase_time_linit --> tu sirf 1 sec hi bol payega, jyada nhi
            # word1 = recognizer.recognize_google(audio)
            print(word1)
            
            if(word1.lower() == "hey buddy"):
                speak("yes Sir")

                # input()
                # if("in youtube" in word1.lower()):
                #      p = "comedy"
                #      webbrowser.open(f"https://www.youtube.com/results?search_query={p}")
                     
                print("h")
                while ("quite" in word1.lower()) == False:
                    print("p")

                    input()
                    print(word1)
                    command(word1)
                    
                speak("quite")
                

                # print("thike")


        except sr.UnknownValueError:
            print("error ")
