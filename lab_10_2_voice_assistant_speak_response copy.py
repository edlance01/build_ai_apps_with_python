import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI()
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
    except sr.RequestError:
        print("Speech service is unavailable.")

def ask_assistant(message):
    response = client.responses.create(
        model="gpt-5-mini",
        input=message
    )
   # return response.output[0].content[0].text
    return response.output_text

user_text = listen()

if user_text:
    reply = ask_assistant(user_text)
    speak(reply)
else:
    speak("I did not catch that.  Please try again.")