import sys
from stats import count_words, count_chars, rearrange_dict

def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
    else:
        path = sys.argv[1]

    book_text = get_book_text(path)
    words = count_words(book_text)
    chars = count_chars(book_text.lower())
    char_dict = rearrange_dict(chars)
    
    print('============ BOOKBOT ============\n')
    print(f'Analyzing book found at {path}...\n')
    print('----------- Word Count ----------\n')
    print(f'Found {words} total words\n')
    print('--------- Character Count -------')
    for ch_dict in char_dict:
        if ch_dict['char'].isalpha():
            print(f'{ch_dict['char']}: {ch_dict['num']}')
    print('\n============= END ===============')
        
main()