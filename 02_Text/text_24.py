# Half the string


def half_string():
    user_string = str(input("Give a string: "))
    if len(user_string) == 0 or user_string.isalpha() is False:
        print("Invalid string")
    elif len(user_string) % 2 == 0:
        half_of_string = int(len(user_string)/2)
        print(user_string[0:half_of_string])
    else:
        print("Odd string")


half_string()
