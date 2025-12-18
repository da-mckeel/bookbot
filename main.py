from stats import count_words, count_letters, sorted_letters

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def print_char_counts(char_list):
    for d in char_list:
        char = d["char"]
        num = d["num"]
        if char.isalpha():
            print(f"{char}: {num}")

def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    letters = count_letters(book_text)
    char_list = sorted_letters(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_counts(char_list)
    print("============= END ===============")

main()