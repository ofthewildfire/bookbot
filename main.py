import sys
from stats import word_count, letter_count, sorted_list, word_count_return

def get_book_text(book_path):
    book_text = ''
    with open(book_path) as f:
        book_text = f.read()
    return book_text



book_path = 'books/frankenstein.txt'

book = get_book_text('books/frankenstein.txt')

word_count(book)

book_letter_count = letter_count(book)

word_count_num = word_count_return(book)



sorted_list_in_reverse = sorted_list(book_letter_count, book_path, word_count_num )


def print_report(sorted_list_in_reverse, book_path, word_count):
    list_string = ''
    for i in sorted_list_in_reverse:
        list_string += f"{i['char']}: {i['num']}\n"
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{list_string}
============= END ===============""")


print_report(sorted_list_in_reverse, book_path, word_count_num)


print(sys.argv)