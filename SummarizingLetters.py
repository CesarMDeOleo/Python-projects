import string

def summarize_letters(text):
    
    cleaned_text = text.lower().translate(str.maketrans("", "", string.punctuation + string.whitespace))

    dictionary = {}
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    tuple = [(letter, dictionary[letter]) for letter in dictionary]

    print( '\n' , tuple, end = '\n')
    print( '\n' , dictionary, end = '\n\n')


    alphabet = set(string.ascii_lowercase)
    letters_in_text = set(cleaned_text)
    all_letters_present = alphabet.issubset(letters_in_text)
        
    if all_letters_present:
        print("The sentence contains all letters of the alphabet.")
    else:
        print("The sentence does not contain all letters of the alphabet.")


sentence = input("Enter the sentence you would like to summarize: ")
summarize_letters(sentence)