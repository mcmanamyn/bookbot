from stats import get_num_words
from stats import count_characters
from stats import sorted_characters
import sys
from sys import argv
import pprint


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    try:
        if len(argv) > 0:
            file_path = argv[1]
            word_count = get_num_words(file_path)
            count = count_characters(file_path)
            
            print(
            f'============ BOOKBOT ============'
            f'\nAnalyzing book found at {file_path}...'
            f'\n----------- Word Count ----------'
            f'\nFound {word_count} total words'
            f'\n--------- Character Count -------'
            f''
            )
            
            od_characters = (sorted_characters(count))
            for key in od_characters:
                print(f'{key}: {od_characters[key]}')
        
    except IndexError:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    except FileNotFoundError:
        print('Error: Book was not found. Perhaps you spelled it wrong.')
        sys.exit(2)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(3)

main()