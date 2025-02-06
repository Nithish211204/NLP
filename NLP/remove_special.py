import re

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

