# Virtual Assistant - Jarvis

A voice-based intelligent virtual assistant built in Python, similar to Alexa or Google Assistant.

## Features
- Voice input using Speech Recognition
- Text-to-Speech responses (pyttsx3 + gTTS)
- Open websites and applications (Google, YouTube, Facebook, etc.)
- Play music from local library
- ChatGPT integration for intelligent responses
- General task handling
  
## Technologies Used
- Python
- speech_recognition
- pyttsx3 and gTTS (for speaking)
- pygame (music ke liye)
- webbrowser
- OpenAI API

## How to Run (Local Setup)

1. Install the required libraries:
   ```bash
   pip install speechrecognition pyttsx3 pyaudio pygame openai gTTS requests
2. Run the Assistant:
   ```bash
   python main.py

## Project Files
- main.py (Main assistant code)
- client.py (ChatGPT integration)
- musicLibrary.py (Music playback)

  
## Challenges & What I learned

Maine ise Pydroid 3 app mein mobile pe develop kiya kyunki mere paas laptop nahi hai. Voice recognition aur API integration mein kaafi errors aaye the, lekin unko fix karke finally working bana diya.
Abhi ye basic version hai. Aage isme aur features add karungi jaise weather update, news, reminders etc.

Made by Urmi Porwal
   B.Tech Computer Science, KNIT Sultanpur
   GitHub: @Urmi-Code-web
