import sys

from stats import counting_character, sort_counted_character, get_num_words, create_report

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])

    num_words = get_num_words(book)

    counted = counting_character(book)

    sorted_character = sort_counted_character(counted)

    create_report(
        sys.argv[1],
        num_words,
        sorted_character
    )

main()