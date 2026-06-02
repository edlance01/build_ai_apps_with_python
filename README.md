

## Labs used for teaching Liam Steele book: Build AI Apps with Python
### - Note some were enhanced / changed
---

## Lab 10
- Needed to install portaudio first in order to get pyaudio to work
    - `brew install portaudio`
    - `pip install pyaudio`


- Also needed to replace this code in ask_assistant function
    - `return response.output[0].content[0].text`
    - `return response.output_text`


### In 10.3 I had a problem with pyttsx3
> This is the classic macOS pyttsx3/NSSpeechSynthesizer issue: the underlying run loop doesn't cleanly restart after the first runAndWait() within the same process, so subsequent engines initialize but produce no audio. Reinitializing isn't enough on its own.
The most reliable fix on macOS is to skip pyttsx3 and call the system say command directly:
pythonimport subprocess

``` 
def speak(text):
    print("Assistant:", text)
    subprocess.run(["say", text])
```

> You can drop import pyttsx3 and the speaker = pyttsx3.init() line entirely. say is built into macOS, handles repeated calls without issue, and respects the voice/rate set in System Settings → Accessibility → Spoken Content. You can pick a voice with ["say", "-v", "Samantha", text] and set rate with ["say", "-r", "180", text].

---