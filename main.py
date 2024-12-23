def get_book_contents(boot_path):
    with open(book_path) as f:
        return f.read()

def word_counter(book_contents):
    words = book_contents.split()
    return len(words)

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

    book_content = get_book_contents(book_path)
    word_count = word_counter(book_content)
    num_of_character = character_counter(book_content)

    print(f"--- Begin report of {book_path} ---")
    for letter, count in num_of_character.items():
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End of report")
    return book_report

book_path = "books/frankenstein.txt"


book_report(book_path)