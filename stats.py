def get_words_number(file_contents):
    word_count = 0
    word_list = []
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

def character_count(file_contents):
    alphabet = {}
    lower_string = file_contents.lower()
    sorted_string = sorted(lower_string,reverse=True)
    for char in sorted_string:
        if char in alphabet and char.isalpha():
            alphabet[char] += 1
        elif char not in alphabet and char.isalpha():
            alphabet[char] = 1
#        else:
#            print(f"ignoring {char}")
    return alphabet

def dict_sort(alphabet):
    sorted_dict = {}
    sorted_dict = dict(sorted(alphabet.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
