import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',170)
engine.setProperty('volume',1.0)
newsapi="536ae05dda1b4522a5ccbd0742698195"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def chatgptProcess(command):
    client=OpenAI(api_key="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")
    completion=client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role":"system","content":"You are a virtual assistant named Jarvis skilled in general tasks like Alexa or google assistant.Give short smart responses"},
            {"role":"user","content":command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music.get(song)
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        output=chatgptProcess(c)
        speak(output)

r = sr.Recognizer()     #speech recognizer functionality lene me nhelp krti h    
if __name__=="__main__":
    speak("Initialising Jarvis....")
    # listen for the word Jarvis
    # Obtain audio from the microphone
    while True:
        print("Recognising")    # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=4)
            word=r.recognize_google(audio)
            if "hello" in word.lower() or "jarvis" in word.lower():
                speak("Yes mam")
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
        except sr.WaitTimeoutError:
            print("You didn't speak anything")
        except Exception as e:
            print("Error; {0}".format(e))