# Pig Latin


def pig_translator(string: str) -> str:
    return string[::-1] + "ay"


def __main_pig_latin(string: str):
    if not string.isalpha():
        print("We only accept letters")
    else:
        print(pig_translator(string))


__main_pig_latin("kalklator")
