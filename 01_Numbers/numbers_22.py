# Neon Number


def sum_of_digits(number):
    str_number = str(number)
    total = 0

    for digit in str_number:
        total += int(digit)
    return total


def neon_tester(number):
    sqr_number = number**2

    if sum_of_digits(sqr_number) == number:
        return True
    else:
        return False


def neon_number_main():
    range_a = input("Give range a: ")
    range_b = input("Give range b: ")

    if range_a.isnumeric() is False or range_b.isnumeric() is False:
        print("Input error")
    elif int(range_a) >= int(range_b):
        print("Range a is greater or equal range b")
    else:
        for number in range(int(range_a), int(range_b)):
            if neon_tester(number):
                print("%d is a Neon Number!" % number)


neon_number_main()
