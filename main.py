from stats import *
import sys

# Check if the number of command-line arguments is not equal to 2
if len(sys.argv) != 2:
    # If not, print a usage message
    print("Usage: python3 main.py <path_to_book>")
    # Exit the program with a status code of 1 to indicate an error
    sys.exit(1)

def get_book_text(filepath):
    """
    Reads the content of a text file and returns it as a string.

    Args:
        filepath (str): The path to the text file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(filepath) as f:
        return f.read()

def generate_report(filepath):
    '''
    Generates a report analyzing the contents of a book.

    This function performs the following operations:
    1. Prints a header indicating the start of the report.
    2. Analyzes the text of a book located at the provided filepath.
    3. Outputs the total word count of the book.
    4. Outputs the character count for each alphabetic character in the book, 
       sorted in descending order of frequency.
    5. Prints a footer indicating the end of the report.

    Args:
        filepath (str): The path to the book file to be analyzed.

    Returns:
        None: This function prints the results directly to the console.
    '''
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_dict = char_counter(book_text)
    ordered_list_of_char_dicts = sort_dict_list(char_dict)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for element in ordered_list_of_char_dicts:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["count"]}")
    
    print("============= END ===============")

def main(): 
    generate_report(sys.argv[1])

main()
    