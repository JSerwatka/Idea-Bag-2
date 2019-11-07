# Typoglycemia

from random import randint, shuffle


def string_sorter1(string: str) -> str:
    middle_string_list = list(string[1:(len(string) - 1)])
    shuffle(middle_string_list)
    middle_string = ''.join(middle_string_list)
    output_string = string[0] + middle_string + string[-1]

    return output_string


def string_sorter2(string: str) -> str:
    sorted_string = list(string)
    middle_string = string[1:(len(string) - 1)]
    used_indexes = [0, (len(string) - 1)]
    new_index = 0

    for letter in middle_string:
        while new_index in used_indexes:
            new_index = randint(1, len(string) - 2)
        used_indexes.append(new_index)
        sorted_string[new_index] = letter

    return "".join(sorted_string)


print(string_sorter2("abcdef"))
