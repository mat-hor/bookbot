from stats import get_num_words, get_num_char, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_content = get_book_text(book_path)
    num_words = get_num_words(file_content)
    char_dict = get_num_char(file_content)
    sorted_char = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char:
        name = char_dict["name"]
        count = char_dict["num"]
        if name.isalpha():
            print(f"{name}: {count}")


main()