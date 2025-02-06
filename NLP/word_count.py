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
# speech_recog()
def check_text(real_text):
    speech_text=speech_recog()
    if real_text.lower() == speech_text.lower() :
        print("GOOD JOB YOU DONE IT :)")
    elif real_text.lower() != speech_text.lower() :
        print("spell it again")
        print(real_text)
        return check_text(real_text)
        

       
# Function to count words in a text file
def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents of the file
            content = file.read()
            # Split the content into words
            words = content.split()
            # Get the total number of words
            word_count = len(words)
            return word_count,words

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

# Specify the path to your text file
def main():
    filename = r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail.txt'

# Get the word count
    word_count,words = count_words_in_file(filename)


    for i in range(0, len(words), 5):
        spell = ""
        if len(words) - i > 5:
            spell = " ".join(words[i:i + 5])
        else:
            spell = " ".join(words[i:])
        print(spell)
        print("Spell the Above Text")
        check_text(spell)
