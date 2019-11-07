# Circular Primes
from math import floor, sqrt


def check_if_prime(n: int) -> bool:
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def check_if_circular_prime(n: int):
    str_num = str(n)
    str_array = [str_num]

    for _ in range(len(str_num) - 1):
        if check_if_prime(int(str_num)):
            str_num = str_num[1:] + str_num[0]
            str_array.append(str_num)
        else:
            return "INPUT {0:s} -> Output[{1:s}] - Invalid".format(str_array[0], " -> ".join(str_array))

    return "INPUT {0:s} -> Output[{1:s}] - Valid".format(str_array[0], " -> ".join(str_array))


print(check_if_circular_prime(991))
