def get_book_text(filepath):
    """
    Reads a file and returns its contents as a string.
    Args:
        filepath (str): Path to the file to be read
    Returns:
        str: Contents of the file
    """
    try:
        # Try UTF-8 encoding first with error replacement
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except UnicodeDecodeError:
        # Fall back to latin-1 which can decode any byte sequence
        with open(filepath, "r", encoding="latin-1", errors="replace") as f:
            return f.read()
        
def get_num_words(text):
    """
    Counts the number of words in the provided text.
    Args:
        text (str): The text to analyze
    Returns:
        int: Number of words in the text
    """
    words = text.split()
    return len(words)
        
def char_count(text):
    """
    Counts the frequency of each character in the provided text.
    Args:
        text (str): The text to analyze
    Returns:
        list: List of dictionaries containing character and count information,
            sorted by count in descending order
    """
    chars = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
                
    chars_list = []
    for char, count in chars.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list of dictionaries by count in descending order
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    return chars_list
        
def print_report(chars_list):
    """
    Prints a formatted report of character frequencies.
    Args:
        chars_list (list): List of dictionaries containing character and count information
    """
    print("--------- Character Count -------")
    for item in chars_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

