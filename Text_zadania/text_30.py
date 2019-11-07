# Voodlewoodlel


def voodle_woodlel(text):
    vowels = "aąeęiouyAĄEĘIOUY"
    new_text = ""

    for letter in text:
        if letter not in vowels:
            new_text += letter
        else:
            if letter.isupper():
                new_text += "Oodle"
            else:
                new_text += "oodle"
    return new_text


def _start_voodle():
    name = str(input("What is your name: "))
    surname = str(input("What is your surname: "))

    print(voodle_woodlel(name))
    print(voodle_woodlel(surname))


_start_voodle()
