import sys

from stats import get_num_words
from stats import count_letter
from stats import sort_dict_by_value

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = get_num_words(text)  
    letter_count = count_letter(text)   
    sorted_letter_count = sort_dict_by_value(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_letter_count:
        print(f"{letter}: {count}")
    print("============ END OF BOOK ============")  
main()