# Find the N-th Natural Number
#todo: zrobic tak, aby znajdowala czescia jakiej liczby jest ta cyfra


def num_string(position: int) -> str:
    digit_string = ""

    for i in range(1, 1001):
        digit_string += str(i)
    print(digit_string)
    return digit_string[position-1]


print(num_string(1986))
