# Scooby Doo

vowels = "aeouiy"


def scooby_doo(string: str) -> list:
    words = string.split(" ")

    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] in vowels:
                words[i] = "r" + words[i][j:]
                break

    return words


print(*scooby_doo("scooby doo"))
