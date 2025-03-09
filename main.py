from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book_text(book_path)
    print(get_num_words(file_content))

main()