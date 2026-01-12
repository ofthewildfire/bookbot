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


def sort_on(list):
    return list['num']


def sorted_list(dict, book_path, word_count):
    let_list = []
    for i in dict:
        if(i.isalpha()):
            dict_create = {"char": i, "num": dict[i]}
            let_list.append(dict_create)
    return let_list.sort(reverse=True, key=sort_on)

                 




