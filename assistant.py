import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import dateparser
import time

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def wishme():
    print("Welcome back!!")
    speak("Welcome back!!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("please tell me how may I help you.")
    print("please tell me how may I help you.")


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\ss\screenshot.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query


if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()

        if "open google" in query:
            wb.open("google.com")

        elif "search on google" in query:
            speak("what want to search")
            search = takecommand()
            wb.open(f"https://www.google.com/search?q={search}")

        elif "close google" in query:
            os.system("taskkill /f /im msedge.exe")
            speak("Closing google")


        elif query == "open chrome":
            wb.open("https://chorome.com")
            speak("Opening Chrome")

        elif query =="search on chrome":
            speak("What do you want to search?")
            query = takecommand()
            wb.open(f"https://www.chorome.com/search?q={query}")

        elif query=="close chrome":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing chrome")

        elif query =="open youtube":
            wb.open("https://www.youtube.com")
            speak("Opening Youtube")

        elif query=="search on youtube":
            speak("What do you want to search?")
            query = takecommand()
            wb.open(f"https://www.youtube.com/results?search_query={query}")

        elif query=="close youtube":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing youtube")

        elif "open instagram" in query:
            wb.open("https://www.instagram.com/")
            speak("Opening Instagram")

        elif "close instagram" in query:
            os.system("taskkill /F /im msedge.exe")


        elif "time" in query:
            time()

        elif "date" in query:
            now = datetime.datetime.now()
            speak(f"Todays date is {now.date()}")


        elif "fine" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "good" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")



        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif query=="close stack overflow":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing stack overflow")

        elif "play music" in query:
            song_dir = "C:\cs music"
            songs = os.listdir(song_dir)
            if not songs:
                speak("No music files found in the specified directory.")
            else:
                print(songs)
                x = len(songs)
                y = random.randint(0, x-1)
                os.startfile(os.path.join(song_dir, songs[y]))


        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "tell me what i say to remember" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "open screenshot" in query:
            ss_path = "C:\\ss\\screenshot.png"
            try:
                os.startfile(ss_path)
                speak("opening Screenshot")
            except Exception as e:
                print(f"error while opening : {e}")
                speak("Screenshot cant open")

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")




        elif "quit" in query or "exit" in query:
            speak("Goodbye have a nice day")
            quit()


