def get_book_text(path_to_file):
    file_contents= "" 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_words_number(file_contents):
    wourd_count = 0
    word_list = []
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count


def main():
    book = get_book_text('books/frankenstein.txt')
    word_count = get_words_number(book)
    print(f"{word_count} words found in the document")

main()
