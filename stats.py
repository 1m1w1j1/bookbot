def get_words_number(file_contents):
    word_count = 0
    word_list = []
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

def character_count(file_contents):
    alphabet = {}
    lower_string = file_contents.lower()
    for char in lower_string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet
