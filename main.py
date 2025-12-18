def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")

main()