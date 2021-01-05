# Username generator

def username_switch(name, surname, version):
    if version == 1:
        return name[0] + surname
    elif version == 2:
        if len(surname) >= 4:
            return name + surname[:4]
        else:
            return name + surname
    elif version == 3:
        if len(name) >= 4:
            return name[:4] + surname
        else:
            return surname + name
    elif version == 4:
        return name[:3] + surname[:3]
    elif version == 5:
        return surname[:3] + name[:3]
    else:
        return "There are no other username sugestions"


def sugestion_automat():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")

    if name.isalpha() or surname.isalpha():
        answer = ""
        version = 1
        while answer != "yes":
            print(username_switch(name.lower(), surname.lower(), version))
            version += 1
            answer = input("Do you like it? yes/no: ")
    else:
        print("Wrong input")
        return


sugestion_automat()