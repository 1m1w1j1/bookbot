import sys
from stats import get_words_number
from stats import character_count
from stats import dict_sort

def get_book_text(path_to_file):
    file_contents= "" 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_args = len(sys.argv)
    if num_args < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_file = sys.argv[1]
    book = get_book_text(text_file)
    word_count = get_words_number(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at location")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    characters = character_count(book)
    sorted_characters = dict_sort(characters)

    print("--------- Character Count -------")
    for key,value in sorted_characters.items():
        print(f"{key}: {value}")
    print("============= END ===============")
main()
