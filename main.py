def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_word_count(text)
    print(f"This document has {word_count} words")
    #count_characters(text)


    
def get_word_count(text):
    words = text.split()
    return len(words)
    
        

def get_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    words = text.split()
    lowered_string = ""
    for word in words:
        lowered_word = word.lower()
        lowered_string += lowered_word
    print(lowered_string)

    



main()
