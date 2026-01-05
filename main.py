from stats import word_count, letter_count, sorted_list

def get_book_text(book_path):
    book_text = ''
    with open(book_path) as f:
        book_text = f.read()
    return book_text



book_path = 'books/frankenstein.txt'

text = get_book_text('books/frankenstein.txt')
word_count(text)
count = letter_count(text)

sorted_list(count, book_path, word_count )

