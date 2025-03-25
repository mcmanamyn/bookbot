from collections import OrderedDict

def get_num_words(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        words = file_contents.split()
        len_words = len(words)
        
        return f'{len_words}'
    
def count_characters(file_path):
    character_dict = {}
    with open(file_path) as file:
        entire_file = file.read()
        words = entire_file.split()
        for word in words:
            letter = str(word)
            
            for character in letter:
                normalized_character = character.lower()
                character_dict[normalized_character] = character_dict.get(normalized_character, 0) + 1
    
    return character_dict

def sorted_characters(character_dict):
    list_of_tuples = []
    tuples = ()
    final_dict = OrderedDict()
    for key in character_dict:
        if key.isalpha():
            tuples = (character_dict[key], key)
            list_of_tuples.append(tuples)
        else:
            pass
    
    sorted_tuples = sorted(list_of_tuples, reverse=True)
    for item in sorted_tuples:
        item_key = item[1]
        item_value = item[0]
        final_dict[item_key] = item_value
        
    return final_dict
