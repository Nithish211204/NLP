import nltk
import streamlit
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize
from word_count import count_words_in_file
from word_read import speak

# Make sure to download necessary NLTK resources
nltk.download('punkt')

def summarize_text(text, word_count):
    # Summarize the text using gensim
    summary = summarize(text, word_count=word_count)
    return summary

def extract_important_points(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Get the summary and split it into sentences
    summary_sentences = sent_tokenize(summarize(text))
    
    # Extract the most important points from the summary
    important_points = summary_sentences[:num_sentences]
    
    return important_points

# Example usage
st.title("SUMMARY OF THE GIVEN TEXT:")
filename = st.text_input("Enter the path to your text file:", r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\summary_text.txt')
    
file=open(r'C:\Users\cheru\OneDrive\Desktop\Hack\text_recog\nithi\summary_text.txt')
text=file.read()


summary = summarize_text(text, count_words_in_file(filename))
important_points = extract_important_points(text, num_sentences=3)

st.write("Summary:\n", summary)
st.write("\nImportant Points:")
for point in important_points:
    st.write("-", point)
