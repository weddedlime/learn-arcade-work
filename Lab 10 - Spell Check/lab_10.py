import re

# Function to split apart words in a string and return them as a list
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# Linear search function
def linear_search(dictionary, word):
    for w in dictionary:
        if w == word:
            return True
    return False

# Binary search function
def binary_search(dictionary, word):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        if dictionary[mid] < word:
            low = mid + 1
        elif dictionary[mid] > word:
            high = mid - 1
        else:
            return True
    return False

def main():
    # Read dictionary
    with open('dictionary.txt', 'r') as file:
        dictionary_list = [line.strip().upper() for line in file]

    print("--- Linear Search ---")
    line_number = 0
    with open('AliceInWonderland200.txt', 'r') as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not linear_search(dictionary_list, word.upper()):
                    print(f"Line {line_number}: {word}")

    print("--- Binary Search ---")
    line_number = 0
    with open('AliceInWonderland200.txt', 'r') as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not binary_search(dictionary_list, word.upper()):
                    print(f"Line {line_number}: {word}")

if __name__ == "__main__":
    main()
