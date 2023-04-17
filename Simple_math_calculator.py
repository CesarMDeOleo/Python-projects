def calculation(math_phrase):

    words = math_phrase.split()

    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    numbers = []
    operation = 'none'

    for word in words:
        if word in number_dict:
            numbers.append(number_dict[word])

    for word in words:
        if word == 'plus':
            operation = '+'
        elif word == 'minus':
            operation = '-'
        elif word == 'times':
            operation = '*'
        elif word == 'divided':
            operation = '/'
        elif word == 'raised':
            operation = '**'
    
    if operation == '+':
        print(numbers[0] + numbers[1])
    elif operation == '-':
        print(numbers[0] - numbers[1])
    elif operation == '*':
        print(numbers[0] * numbers[1])
    elif operation == '/':
        print(numbers[0] / numbers[1])
    elif operation == '**':
        print(numbers[0] ** numbers[1])
    

main_math_phrase = input("Enter a math phrase: ")
calculation(main_math_phrase)