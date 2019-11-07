# Find Pi to the Nth Digit
# todo: zamienić zwykłe pi na nieskończony ciąg ze wzoru

from math import pi

def pi_to_nth() -> str:
    nth_digit = input("Do którego miejsca podać pi: ")
    output_pi = ""

    for digit in range(0, int(nth_digit)+2):
        output_pi += str(pi)[digit]

    return output_pi


print(pi_to_nth())