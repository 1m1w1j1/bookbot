def get_num_words(text):
    return len(text.split())


def count_letter(text):
    lower_text = text.lower()
    letter_count = {}
    for char in lower_text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
        else:
            continue
    return letter_count

def sort_dict_by_value(letter_count):
    sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_letter_count  
    
    