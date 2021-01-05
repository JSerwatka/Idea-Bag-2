# Rovarspraket

import re

consonants = "bcdfghjklmnpqrstvwxyz"


def text_to_rovar(string: str) -> str:
    index = 0

    while index < len(string):
        if string[index] in consonants:
            string = string[:index + 1] + 'o' + string[index] + string[index + 1:]
            index += 3
        else:
            index += 1

    return string


def rovar_to_text(string: str) -> str:
    pattern = r"([%s])o\1|^[%s]$" % (consonants, consonants)
    return re.sub(pattern, lambda x: x.group(1), string)


print(text_to_rovar(input()))
print(rovar_to_text(input()))
