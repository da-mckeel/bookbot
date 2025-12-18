def get_book_text(f):
    file_contents = f.read()
    return file_contents

def num_of_words(f):
    file_contents = f.read()
    words = file_contents.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        word_count = num_of_words(f)
        return print(f"Found {word_count} total words")

main()