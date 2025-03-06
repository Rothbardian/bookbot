import sys
from stats import get_book_text, get_num_words, char_count, print_report

def main():
    # Check if a filepath is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: No filepath provided.")
        print("Usage: python main.py <filepath>")
        return
    
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    
    # Get the text content from the file
    text = get_book_text(filepath)
    
    # Count the words
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    
    # Count the characters
    chars_list = char_count(text)
    
    # Print the character count report
    print_report(chars_list)
    
if __name__ == "__main__":
    main()

