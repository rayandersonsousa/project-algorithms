def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    elif low_index > high_index:
        return True
    elif word[high_index] == word[low_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
