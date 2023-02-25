import string


def is_palindrome(word):
    word = word.lower().translate(str.maketrans("", "", string.punctuation + string.whitespace))

    if word == word[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

if is_palindrome(word):
    print("The word '" + word + "' is a palindrome.")
else:
    print("The word '" + word + "' is not a palindrome.")
