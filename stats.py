# Count words in book
def word_count(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")


# Return the number
def word_count_return(book_text):
    num_words = len(book_text.split())
    return num_words

# Count letters in book
def letter_count(text):
    count = {}
    textLower = text.lower()
    for i in textLower:
        if i in count:
            count[i.lower()] = count[i.lower()] + 1
        else:
            count[i.lower()] = 1
    return count

# Sort list function
def sort_on(list):
    return list['num']


# Sorted list function
def sorted_list(dict, book_path, word_count):
    let_list = []
    for i in dict:
        if(i.isalpha()):
            dict_create = {"char": i, "num": dict[i]}
            let_list.append(dict_create)
    return (sorted(let_list, key=sort_on, reverse=True))
                 


# https://realpython.com/sort-python-dictionary/#using-the-key-parameter-and-lambda-functions 
# >>> people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# >>> # Sort key
# >>> def value_getter(item):
# ...     return item[1]
# ...

# >>> sorted(people.items(), key=value_getter)
# [(2, 'Jack'), (4, 'Jane'), (1, 'Jill'), (3, 'Jim')]

# >>> # Or with a lambda function
# >>> sorted(people.items(), key=lambda item: item[1])
# [(2, 'Jack'), (4, 'Jane'), (1, 'Jill'), (3, 'Jim')]



