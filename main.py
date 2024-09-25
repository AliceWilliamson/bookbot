def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_word_count(text)
    char_count = count_characters(text)
    sorted_char_list = get_sorted_list(char_count)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")
    
    print("--- End report ---")




    
def get_word_count(text):
    words = text.split()
    return len(words)
    
def sort_on(d):
    return d["num"]

def get_text(path):
    with open(path) as f:
        return f.read()


def get_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num" : num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] +=1
            pass
    return letter_counts


main()
