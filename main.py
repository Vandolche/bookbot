import sys
from stats import word_count
from stats import char_count
from stats import sort_char_dic

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    
    return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = word_count(book_content)
    chars = char_count(book_content)
    list_dic = sort_char_dic(chars)
    
    print(f"============ BOOKBOT ============\n"
    f"Analyzing book found at {book_path}\n"
    f"----------- Word Count ----------\n"
    f"Found {num_words} total words\n"
    f"--------- Character Count -------")
    for dic in list_dic:
        if dic['char'].isalpha():
            print(f"{dic['char']}: {dic['num']}")



main()