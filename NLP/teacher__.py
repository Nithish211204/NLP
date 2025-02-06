# import streamlit as st
# import pyttsx3
# # pip_install pyttsx3
# import os
# import re
# import speech_recognition as sr


# def speak(text):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()
    
#     # Use the engine to speak the text
#     engine.say(text)
    
#     # Run the speech engine
#     engine.runAndWait()
#     check_text(text)

# # Call the function
# # speak()


# def remove_special_characters(file_path):
#     f=open(file_path)
#     text=f.read()
    
#     # This pattern matches any character that is not a letter, number, or space
    
#     pattern = r'[^a-zA-Z0-9\s]'
#     # Replace all matched characters with an empty string
#     cleaned_text = re.sub(pattern, ' ', text)
#     with open(file_path, 'w') as file:
#         file.write(cleaned_text)
    
#     return file_path


# # pip install streamlit

# def speech_recog():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Please speak something...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#         try:
#             text = recognizer.recognize_google(audio)
#             st.write(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             st.write("Sorry, I could not understand the audio.")
#         except sr.RequestError:
#             st.write("Could not request results; check your network connection.")
#         return ""


# def check_text(text):
#     #teacher response and student response checker
#     st.write("student response")
#     speech_text = speech_recog()
#     real_text = text
#     if speech_text.lower() != real_text.lower():
#         st.write("Expected response:"+ real_text)
#         speak(text)
#     elif speech_text == "continue master" :
#         st.write(f"Your skipped text:"+{real_text})  
#     elif speech_text.lower() == real_text.lower() :
#         st.write("Well done")
#         x=0
#     else:
#         check_text(text)
        
    
#           # Recursive call to allow retry

# def count_words_in_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()
#             word_count = len(words)
#             return word_count, words
#     except FileNotFoundError:
#         st.write(f"Error: The file {filename} was not found.")
#         return None, []


# def main():
#     st.title("TEXT DICTATOR AND TEXT CHECKER")
    
#     # File input
#     file_path=r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail.txt'
#     new_file_path=r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail_modified.txt'
#     f=open(file_path)
#     text=f.read()
#     with open(new_file_path, 'w') as file:
#         file.write(text)
    
#     filename = st.text_input(" Give the path of the file : " ,r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail_modified.txt')
    
#     filename=remove_special_characters(filename)

#     if filename:
#         word_count, words = count_words_in_file(filename)
#         if word_count is not None:
#             st.write(f"The file contains {word_count} words.")
#             for i in range(0, len(words), 5):
#                 st.write("Teacher")
#                 spell = ""
#                 if len(words) - i > 5:
#                     spell = " ".join(words[i:i + 5])
#                 else:
#                     spell = " ".join(words[i:])
#                 st.write(spell)
#                 st.write("Spell the above text or to skip 'CONTINUE MASTER'")
#                 speak(spell)

# if __name__ == "__main__":
#     main()
import streamlit as st
import pyttsx3
import os
import re
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def remove_special_characters(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        with open(file_path, 'w') as file:
            file.write(cleaned_text)
        return file_path
    except FileNotFoundError:
        st.write(f"File not found: {file_path}")
        return ""

def speech_recog():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.write("Network error.")
        return ""

def check_text(text):
    st.write("Expected response")
    speech_text = speech_recog()
    if speech_text.lower() != text.lower():
        st.write("Expected response: " + text)
        speak(text)
    elif speech_text.lower() == "continue master":
        st.write(f"Skipped text: {text}")
    else:
        st.write("Well done!")

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words), words
    except FileNotFoundError:
        st.write(f"Error: File {filename} not found.")
        return None, []

def main():
    st.title("Text Dictator and Checker")
    file_path = st.text_input("Enter file path:", "example.txt")
    if os.path.exists(file_path):
        file_path = remove_special_characters(file_path)
        word_count, words = count_words_in_file(file_path)
        if word_count:
            st.write(f"The file contains {word_count} words.")
            for i in range(0, len(words), 5):
                spell = " ".join(words[i:i + 5])
                st.write("Teacher says: " + spell)
                speak(spell)
                st.write("Now you repeat...")
                check_text(spell)

if __name__ == "__main__":
    main()
