def get_num_words(file_content):
    list_of_words = file_content.split()
    num_words = len(list_of_words)
    return f"{num_words} words found in the document"
