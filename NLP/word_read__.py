import streamlit as st
import pyttsx3
# pip_install pyttsx3
import speech_recognition as sr


def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Use the engine to speak the text
    engine.say(text)
    
    # Run the speech engine
    engine.runAndWait()
    check_text(text)

# Call the function
# speak()



# pip install streamlit

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


def check_text(text):
    speech_text = speech_recog()
    if speech_text == "repeat master":
        st.write("Your response\t 'REPEAT MASTER' to repeat\t 'CONTINUE MASTER' to continue ")
        speak(text)
    elif speech_text == "continue master" :
        st.write("Your response\t 'REPEAT MASTER' to repeat\t 'CONTINUE MASTER' to continue ")
        x=0
    else:
        check_text(text)
        
    
          # Recursive call to allow retry

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
    st.title("TEXT OR NOTES DICTATOR")
    
    # File input
    filename = st.text_input("Enter the path to your text file:", r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\trail.txt')
    

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
                # st.write("Spell the above text")
                st.write("Your response\t 'REPEAT MASTER' to repeat\t 'CONTINUE MASTER' to continue ")
                speak(spell)

if __name__ == "__main__":
    main()