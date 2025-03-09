from stats import get_num_words, get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book_text(book_path)
    num_words = get_num_words(file_content)
    print(f"{num_words} words found in the document")
    print(get_num_char(file_content))

main()