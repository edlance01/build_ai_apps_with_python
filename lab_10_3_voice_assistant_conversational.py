import speech_recognition as sr
import pyttsx3
from openai import OpenAI

"""
This version keeps listening until you tell it to stop
"""
client = OpenAI()
recognizer = sr.Recognizer()
speaker = pyttsx3.init()


# def speak(text):
#     print("Assistant:", text)
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

import subprocess


def speak(text):
    print("Assistant:", text)
    subprocess.run(["say", "Samantha", text])


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        # print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        # print("Speech service is unavailable.")
        return ""


def ask_assistant(message):
    try:
        response = client.responses.create(model="gpt-5-mini", input=message)
        return response.output_text
    except Exception as e:
        print("API error:", e)
        return "Sorry, something went wrong."


speak("Voice assistant online.  Say goodbye to stop.")

while(True):
    user_text = listen()

    if not user_text:
        speak("I did not catch that.")
        continue

    if "goodbye" in user_text.lower():
        speak("Goodbye.")
        break

    reply = ask_assistant(user_text)
    speak(reply)
