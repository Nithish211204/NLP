# Here is a simple code for a text-to-speech converter in Python using the gTTS (Google Text-to-Speech) library:
# pip install gtts mpg321

from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(r"C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\output.mp3")
    os.system("mpg321 output.mp3")
f=open(r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\output_text.txt','r')
text=f.read()
# text = input("Enter the text you want to convert to speech: ")
text_to_speech(text)


# To use this code, you'll need to install the gTTS library and the mpg321 player (to play the output MP3 file). You can install them using pip:

# import sys
# print(sys.executable)

# C:\Users\cheru\OneDrive\Desktop\test\test\env\Lib\site-packages


# This code will take the text as input, convert it to speech using gTTS, save the audio to an MP3 file, and then play the file using mpg321.

# If you want to use a more advanced text-to-speech engine like Amazon Polly or Google Cloud Text-to-Speech, you'll need to install their respective libraries and set up an account with them.

# Let me know if you have any questions or need further assistance!