def get_num_words(file_content):
    list_of_words = file_content.split()
    num_words = len(list_of_words)
    return num_words

def get_num_char(file_content):
    char_dict = {}
    for char in file_content:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    sorted_char_list = []
    for key in char_dict:
        sorted_char_list.append(
            {
                "name": key,
                "num": char_dict[key]
            }
        )
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list
