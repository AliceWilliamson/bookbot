def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_word_count(text)
    print(f"This document has {word_count} words")


    
def get_word_count(text):
    counter = 0
    words = text.split()
    return len(words)
    
        

def get_text(path):
    with open(path) as f:
        return f.read()






main()
