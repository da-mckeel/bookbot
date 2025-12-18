from stats import count_words, count_letters, sorted_letters

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    letters = count_letters(book_text)
    # print(letters)
    char_list = sorted_letters(letters)
    print(char_list)

main()