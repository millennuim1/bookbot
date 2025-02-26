import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

from stats import get_num_words
from stats import count_Characters
from stats import sort_on

def main():
    book_name = sys.argv[1]
    book_text = get_book_text(book_name)
    num_of_words = get_num_words(book_text)
    num_of_char = count_Characters(book_text)
    sort = sort_on(num_of_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    chars_list = []
    for char, num in num_of_char.items():
        chars_list.append({char: num})
    chars_list.sort(reverse=True, key=sort_on)
    for char_dict in chars_list:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

main()