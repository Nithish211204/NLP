import streamlit as st
import speech_recognition as sr
import os
import re

# pip install streamlit


def remove_special_characters(file_path):
    f=open(file_path)
    text=f.read()
    
    # This pattern matches any character that is not a letter, number, or space
    
    pattern = r'[^a-zA-Z0-9\s]'
    # Replace all matched characters with an empty string
    cleaned_text = re.sub(pattern, ' ', text)
    with open(file_path, 'w') as file:
        file.write(cleaned_text)
    
    return file_path


def speech_recog():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.write("Could not request results; check your network connection.")
        return ""

def check_text(real_text):
    speech_text = speech_recog()
    if real_text.lower() == speech_text.lower():
        st.write("GOOD JOB! YOU DID IT :)")
    else:
        st.write("Spell it again")
        st.write(f"Expected: {real_text}")
        check_text(real_text)  # Recursive call to allow retry

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count, words
    except FileNotFoundError:
        st.write(f"Error: The file {filename} was not found.")
        return None, []

def main():
    st.title("Speech Recognition and Text Matching")
    
    file_path=r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail.txt'
    new_file_path=r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail_modified.txt'
    f=open(file_path)
    text=f.read()
    with open(new_file_path, 'w') as file:
        file.write(text)
    
    filename = st.text_input(" Give the path of the file : " ,r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail_modified.txt')
    
    filename=remove_special_characters(filename)

    if filename:
        word_count, words = count_words_in_file(filename)
        if word_count is not None:
            st.write(f"The file contains {word_count} words.")
            for i in range(0, len(words), 5):
                spell = ""
                if len(words) - i > 5:
                    spell = " ".join(words[i:i + 5])
                else:
                    spell = " ".join(words[i:])
                st.write(spell)
                st.write("Spell the above text")
                check_text(spell)

if __name__ == "__main__":
    main()
