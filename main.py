from stats import get_words_number
from stats import character_count
from stats import dict_sort

def get_book_text(path_to_file):
    file_contents= "" 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
#    location = path_to_file
    book = get_book_text('books/frankenstein.txt')
    word_count = get_words_number(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at location")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    characters = character_count(book)
    sorted_characters = dict_sort(characters)
#    print(sorted_characters)
    print("--------- Character Count -------")
    for key,value in sorted_characters.items():
        print(f"{key}: {value}")
    print("============= END ===============")
main()
