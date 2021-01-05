# Next prime number
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


def next_prime(number: int):
    while True:
        number += 1
        if check_if_prime(number):
            print(number)
            choice = input("Find next? T/N \n")
            if choice == 'Y':
                continue
            elif choice == "N":
                break


next_prime(1660)
