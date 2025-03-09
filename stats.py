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