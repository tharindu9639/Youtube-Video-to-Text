import re

def find_hate_text(text):
    # Define a set of keywords or patterns associated with hate speech
    hate_keywords = {'hate', 'discrimination', 'offensive', 'insult', 'threat'}

    # Initialize a list to store found hate words
    found_hate_words = []

    # Check if any hate keywords are present in the text
    for keyword in hate_keywords:
        if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
            found_hate_words.append(keyword)

    return found_hate_words

try:
    # Read the content from the "ConvertText.txt" file
    with open("ConvertText.txt", 'r') as file:
        transcript_text = file.read()

    # Check for hate text
    found_hate_words = find_hate_text(transcript_text)

    if found_hate_words:
        print("Potentially hateful content found in the transcript. Hate words:")
        for word in found_hate_words:
            print(f"- {word}")
    else:
        print("No potentially hateful content found in the transcript.")
except FileNotFoundError:
    print("Error: 'ConvertText.txt' file not found.")
except Exception as e:
    print(f"An error occurred: {e}")