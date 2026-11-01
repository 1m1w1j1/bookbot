from stats import (
    get_word_count,
    get_character_count,
    sort_on,
    chars_dict_to_sorted_list
)

import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path: str, word_count: int, sorted_characters):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if str.isalpha(character[0]):
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")


def main() -> None:
  
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] 
        book = get_book_text(book_path)
        num_words = get_word_count(book)
        character_dictionary = get_character_count(book)
        sorted_dictionary_list = chars_dict_to_sorted_list(character_dictionary)
        return print_report(book_path, num_words, sorted_dictionary_list)

main()
