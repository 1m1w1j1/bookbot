from stats import get_words_number
from stats import character_count


def get_book_text(path_to_file):
    file_contents= "" 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text('books/frankenstein.txt')
    word_count = get_words_number(book)
    print(f"{word_count} words found in the document")
    characters = character_count(book)
    print(characters)
main()
