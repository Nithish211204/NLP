# pip install SpeechRecognition pyaudio

import speech_recognition as sr
import distutils
def speech_recog():
# Initialize the recognizer
    recognizer = sr.Recognizer()

# Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Please speak something...")
        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"you said:{text}")
            return text
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
# 
speech_recog()