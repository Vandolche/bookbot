def word_count(book_contents):
    word_list = book_contents.split( )
    return len(word_list)

def char_count(book_contents):
    char_count = {}
    for char in book_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_char_dic(char_count):

    def sort_on(items):
        return items["num"]

    list_dic = [{"char": i, "num": e} for i,e in char_count.items()]
    list_dic.sort(reverse=True, key=sort_on)

    return list_dic
