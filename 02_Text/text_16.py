# wersja pierwsza
def if_palindrom(string):
    gnirts = ''
    if string.isalpha() is False:
        print("It's not a word")
    else:
        for index in range(len(string)):
            gnirts += (string[(len(string)-1)-index])
        if gnirts == string:
            print("Palindorom")
        else:
            print("Not Palindrom")


# wersja druga
def if_palindrom_2(string):
    if string.isalpha() is False:
        print("It's not a word")
    else:
        if string[::-1] == string:
            print("Palindorom")
        else:
            print("Not Palindrom")


if_palindrom("kajak")
if_palindrom_2("marmomram")
