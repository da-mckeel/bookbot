from stats import count_words, count_letters, sorted_letters
import sys

def entry_check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text():
    with open(sys.argv[1]) as f:
        return f.read()

def print_char_counts(char_list):
    for d in char_list:
        char = d["char"]
        num = d["num"]
        if char.isalpha():
            print(f"{char}: {num}")

def main():
    entry_check()
    book_text = get_book_text()
    word_count = count_words(book_text)
    letters = count_letters(book_text)
    char_list = sorted_letters(letters)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_counts(char_list)
    print("============= END ===============")

main()