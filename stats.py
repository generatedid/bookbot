def get_num_words(text):
    '''
    Returns the number of words in a given string.

    Args:
        text (str): The input string whose words are to be counted.

    Returns: 
        int: The number of words in the input string.

    Example:
        >>> get_num_words("Hello world!")
        2
    '''
    return len(text.split())


def char_counter(text):
    '''
    Counts the frequency of each character in a given string, ignoring case.

    Args:
    text (str): The input string whose characters are to be counted.

    Returns:
    dict: A dictionary where keys are characters and values are the number of 
    occurrences of each character in the input string.

    Example:
    >>> char_counter("Hello World")
    {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    '''
    char_count = dict()
    for e in text.lower():
        if e in char_count:
            char_count[e] += 1
        elif e not in char_count:
            char_count[e] = 1
    return char_count


def sort_dict_list(char_dict):
    '''
    Takes a dictionary characters and their counts and returns a sorted list of dictionaries.

    Args:
    char_dict (dict): A dictionary of characters and their counts.

    Returns:
    sorted_list: A sorted list of dicts made of two key-value pairs: one for the character itself 
    and one for that character's count.
    '''
    # turn char dict into list of dicts
    sorted_dicts = []
    # Creating unsorted dicts list
    for key, value in char_dict.items():
        sorted_dicts.append({"char" : key, "count" : value})
    # Helper func to get the count of the individual character
    def get_key(dict):
        return dict["count"]
    # Sorting dicts list
    sorted_dicts.sort(reverse=True, key=get_key)
    return sorted_dicts
    
