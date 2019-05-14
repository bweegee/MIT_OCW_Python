# Write a program that computes and prints the nth prime number.


def find_prime():
    primes = 1
    is_prime = True
    counter = 1
    value = 2

    print('Enter the nth prime number you want to find')
    n = int(input())

    # loop throug odd numbers to check for potential prime numbers
    while (primes < n):
        counter += 2
        # check if odd number is a prime
        for i in range(2, counter, 1):
            if (counter % i == 0):
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime is True:
            primes += 1
            value = counter
    print(value)


find_prime()
