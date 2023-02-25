def sieve_of_eratosthenes(numbers):

    primes = [True for _ in range(numbers + 1)]
    index = 2
    while index**2 <= numbers:
        if primes[index] == True:
            for i in range(index**2, numbers + 1, index):
                primes[i] = False
        index += 1

    return [index for index in range(2, numbers) if primes[index]]


print(sieve_of_eratosthenes(15000))