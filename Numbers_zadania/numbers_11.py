# Prime factorization
# można korzystać z bardziej wyrafinowanych algorytmów
#
# algorytm z którego korzystam:
# Given an input number n
# check whether any prime integer m from 2 to √n evenly divides n (the division leaves no remainder)
# If n is divisible by any m then n is composite, otherwise it is prime


from math import floor, sqrt


def check_if_prime(n: int) -> bool:
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def next_prime(number: int) -> int:
    while True:
        number += 1
        if check_if_prime(number):
            return number


def find_primes(number: int):
    prime_factor = 1
    number_primes = []

    while not check_if_prime(number):
        prime_factor = next_prime(prime_factor)
        if number % prime_factor == 0:
            number /= prime_factor
            number_primes.append(prime_factor)
            prime_factor = 1
    number_primes.append(int(number))

    return number_primes


print(find_primes(225678))
