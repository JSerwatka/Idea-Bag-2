# Happy numbers


def square_sum(number: int) -> int:
    digit_sum = 0
    text_str = str(number)

    for digit in text_str:
        digit_sum += int(digit)**2

    return digit_sum


def happy_numbers(number: int):
    loop_count = 0

    if number < 0:
        raise ValueError
    else:
        temp_value = square_sum(number)
        while temp_value != 1:
            temp_value = square_sum(temp_value)
            loop_count += 1
            if loop_count > 100000:
                return False

    return True


def happy_finder(amount: int):
    number = 0
    counter = 0

    while counter < amount:
        number += 1
        if happy_numbers(number) is True:
            counter += 1
            print("%d is a happy number" % number)
