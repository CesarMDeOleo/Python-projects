def list_of_integers(numbers):

    number_frequency = {}
    unique_intergers_in_list = set(numbers)
    missing_intergers_in_list = (set(range(1, max(numbers) + 1)) - unique_intergers_in_list)

    for number in unique_intergers_in_list:
        number_frequency[number] = numbers.count(number)

    sorted_numbers = sorted(unique_intergers_in_list, reverse=True)

    print("Number\tFrequency")
    for number in sorted_numbers:
        print(f"{number}\t{number_frequency[number]}")

    print("\nMissing numbers:", missing_intergers_in_list, end="\n")

    return (number_frequency, sorted_numbers)


list = [3, 8, 4, 3, 1, 4, 1, 4]
print(list_of_integers(list))