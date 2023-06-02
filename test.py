from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background = "lightblue")

label = Label(root, text = "Welcome To Your Personal Desktop Assitant", bg = "lavender", fg = "darkblue", font = ("Comic", 30, "bold"))
label.place(relx = 0.5, rely = 0.12, anchor = CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speech_recognisor = sr.Recognizer()
    speak("How can I help you today?")
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognisor.recognize_google(audio, language = 'en-in')
        except sr.UnknownValueError:
                print("Pardon me, please say again, thank you for your patience")
                speak("Pardon me, please say again, thank you for your patience")
                r_audio()
        respond(voice_data)
    
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Ella")
        print("🖤 My name is Ella 🖤")

    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)

    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://www.google.com/")

    if "videos" in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.get().open("https://www.youtube.com/")

    if "text editor" in voice_data:
        speak("Opening Note Pad")
        print("Opening Note Pad")
        subprocess.Popen(["notepad.exe"])



btn = Button(root, text = "Access Personal Assitant", bg = "lavender", fg = "darkblue",
padx = 10, pady = 1, font = ("Comic", 12, "bold"), relief = FLAT, command = r_audio)

btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()