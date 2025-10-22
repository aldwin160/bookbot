from stats import get_num_words, get_num_characters, sorted_char_count

import sys


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        pathstring = f.read()
        return pathstring


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(book_text)


# main()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print(get_num_words(get_book_text(sys.argv[1])))
    list_of_dict = sorted_char_count(get_num_characters(get_book_text(sys.argv[1])))
    for d in list_of_dict:
        for k, v in d.items():
            print(f"{k}: {v}")
    print(sys.argv)
# print(get_num_characters(get_book_text("books/frankenstein.txt")))
