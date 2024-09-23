def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_word_count(text)
    print(f"This document has {word_count} words")
    char_count = count_characters(text)
    print(f"this is the breakdown of letters in the document: {char_count}")



    
def get_word_count(text):
    words = text.split()
    return len(words)
    
        

def get_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] +=1
            pass
    sorted_dict = {k: letter_counts[k] for k in sorted(letter_counts)}
    return sorted_dict


main()
