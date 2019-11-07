# Guess the number
# todo: mozna tez wprowadzic szukanie liczby zawsze w polowie przedzialu, jako lepszej metody sortowania
from random import randrange


def interface() -> str:
    print("Imagine a number and tell me the range in which I should look for it \n")
    guess_low = int(input("Minimum: "))
    guess_max = int(input("Maximum: ")) + 1

    while True:
        if guess_low >= guess_max or guess_low < 0 or guess_max < 0:
            return "Error: wrong range"
        guess_number = randrange(guess_low, guess_max)
        print(guess_number)
        prompt = input("too high/too low/ok \n")
        if prompt == "too low":
            guess_low = guess_number + 1
        elif prompt == "too high":
            guess_max = guess_number
        elif prompt == "ok":
            return "Your number is %d" % guess_number
        else:
            print("wrong input")


print(interface())
