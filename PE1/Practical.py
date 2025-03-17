import re
from collections import Counter

def count_unique_words(text):
    # Define words to exclude
    exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    
    # Tokenize words (remove punctuation and split by whitespace)
    words = re.findall(r"\b\w+\b", text)
    
    # Filter out excluded words and count occurrences
    filtered_words = [word for word in words if word.lower() not in exclude_words]
    word_counts = Counter(filtered_words)
    
    # Separate lowercase and uppercase words
    lower_case_words = sorted((word, count) for word, count in word_counts.items() if word.islower())
    upper_case_words = sorted((word, count) for word, count in word_counts.items() if word[0].isupper())
    
    # Print formatted output
    for word, count in lower_case_words:
        print(f"{word.ljust(10)} - {count}")
    for word, count in upper_case_words:
        print(f"{word.ljust(10)} - {count}")
    
    print(f"Total words filtered: {sum(word_counts.values())}")

# Example usage
text = input("Enter a string statement:\n")
count_unique_words(text)