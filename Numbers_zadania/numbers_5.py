# Coin flip simulation


from random import randint


def main_program():
    tails = 0
    heads = 0
    decision = ''

    while decision != 'n':
        decision = input("Next flip? (y/n): ")
        if decision == 'n':
            break
        elif decision == 'y':
            coin = randint(0, 1)

            if coin == 0:
                tails += 1
            else:
                heads += 1
            print("%d tails, %d heads \n" % (tails, heads))
        else:
            print("Wrong input. Try Again.")


main_program()
