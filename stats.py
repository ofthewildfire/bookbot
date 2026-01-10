def word_count(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")


def letter_count(text):
    count = {}
    textLower = text.lower()
    for i in textLower:
        if i in count:
            count[i.lower()] = count[i.lower()] + 1
        else:
            count[i.lower()] = 1
    return count


def sorted_list(dict, book_path, word_count):
    let_list = []
    for i in dict:
        if(i.isalpha()):
            let_list.append(f"char: {i}, num: {dict[i]}")
    print(sorted(let_list))
#         print(f"""============ BOOKBOT ============
# Analyzing book found at {book_path}...
# ----------- Word Count ----------
# Found {word_count} total words
# --------- Character Count -------
# char: {i}, num: {dict[i]}
# ============= END ===============""")

                 

        


