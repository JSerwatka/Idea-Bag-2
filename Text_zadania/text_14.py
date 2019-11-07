# Reverse a String


def reverse_string(string):
    gnirts = ''
    if string.isalpha() is False:
        print("It's not a word")
    else:
        for index in range(len(string)):
            gnirts += (string[(len(string)-1)-index])
        return gnirts


def reverse_string_2(string):
    if string.isalpha() is False:
        print("It's not a word")
    else:
        return string[::-1]


print(reverse_string("test"))
print(reverse_string_2("testujemy"))
