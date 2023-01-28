palindrome = float(input("\nEnter a number: "))

normal_number = palindrome
reverse_number = 0

while (palindrome > 0):
    digit = palindrome % 10
    reverse_number = reverse_number * 10 + digit
    palindrome //= 10

if (normal_number == reverse_number):
    print(f'\n{normal_number} is a palindrome.\n')
else:
    print(f'\n{normal_number} is not a palindrome.\n')