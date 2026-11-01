def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_character_count(text: str) -> dict[str, int]:
    character_dictionary = {}
    text_lower_case = text.lower()
    for character in text_lower_case:
        if character in character_dictionary:
            character_dictionary[character] +=1
        else:
            character_dictionary[character] = 1
    return character_dictionary


def sort_on(character:tuple[str, int]) -> int:
    return character[1]


def chars_dict_to_sorted_list(character_dictionary: dict[str, int]) -> list[tuple[str, int]]:
    character_list = []

    for character in character_dictionary:
        character_tuple = (character, character_dictionary[character])
        character_list.append(character_tuple)
    
    sorted_list = sorted(character_list, key=sort_on, reverse=True)

    return sorted_list
