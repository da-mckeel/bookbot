def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_text = text.lower()
    letters = {}
    for l in lower_text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_on(items):
    return items["num"]

def sorted_letters(char_counts):
    letters = []
    for char in char_counts:
        num = char_counts[char]
        letter_dict = {
            "char": char,
            "num": num
        }
        letters.append(letter_dict)
    letters.sort(reverse=True, key=sort_on)
    return letters