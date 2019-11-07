# Disemvoweler

vowels = "aąeęiouyAĄEĘIOUY"


def disemvowel(string: str) -> str:
    no_vowel = ""
    yes_vowel = ""

    for letter in string:
        if letter in vowels:
            yes_vowel += letter
        elif letter.isspace():
            pass
        else:
            no_vowel += letter
    output_string = no_vowel.lower() + " " + yes_vowel.lower()

    return output_string


print(disemvowel("Hello world"))
