def get_book_contents():
    with open(book_path) as f:
        return f.read()

def word_counter(book_contents):
    words = book_contents.split()
    return len(words)

def common_words(book_contents):
    words = book_contents.lower().split()
    most_used_word = ""
    times_word_used = float("-inf")
    count = {}

    for word in words:
        if word not in count:
            count[word] = 0
        count[word] += 1

        if count[word] > times_word_used:
            times_word_used = count[word]
            most_used_word = word
    return most_used_word, times_word_used

def character_counter(book_contents):
    book_contents = book_contents.lower()
    count = {}

    for character in book_contents:
        if character.isalpha():
            if character not in count:
                count[character] = 0
            count[character] += 1
    alphabetical_count = dict(sorted(count.items()))
    return alphabetical_count


def book_report(book_path):

    book_content = get_book_contents()
    word_count = word_counter(book_content)
    num_of_character = character_counter(book_content)
    most_common_word, times_word_used = common_words(book_content)

    print(f"--- Begin report of {book_path} ---")
    print(f"   There are a total of {word_count} words in this book")
    print(f"The most used word is '{most_common_word}', it was used {times_word_used} times")
    for letter, count in num_of_character.items():
        print(f"    The letter '{letter}' was used {count} times")
    print(f"--- End of report ---")
    return book_report

book_path = "books/frankenstein.txt"


book_report(book_path)