# Morse code maker
import winsound

morse_letters = {
    "a": "•—",
    "ą": "•—•—",
    "b": "—•••",
    "c": "—•—•",
    "ć": "—•—••",
    "d": "—••",
    "e": "•",
    "ę": "••—••",
    "f": "••—•",
    "g": "——•",
    "h": "••••",
    "i": "••",
    "j": "•———",
    "k": "—•—",
    "l": "•—••",
    "ł": "•—••—",
    "m": "——",
    "n": "—•",
    "ń": "——•——",
    "o": "———",
    "ó": "———•",
    "p": "•——•",
    "q": "——•—",
    "r": "•—•",
    "s": "•••",
    "ś": "•••—•••",
    "t": "—",
    "u": "••—",
    "v": "•••—",
    "w": "•——",
    "x": "—••—",
    "y": "—•——",
    "z": "——••",
    "ż": "——••—•",
    "ź": "——••—"
}


def string_to_list(string: str) -> list:
    string_list = []

    for element in string.lower():

        if element.isspace():
            string_list.append(" ")
        else:
            for letter in morse_letters:
                if letter == element:
                    string_list.append(morse_letters[letter])

    return string_list


def play_sound(x: str):
    if x == '—':
        winsound.PlaySound('1_morse_code', winsound.SND_FILENAME)
    elif x == '•':
        winsound.PlaySound('0_morse_code', winsound.SND_FILENAME)
    elif x == ' ':
        winsound.PlaySound('w_morse_code', winsound.SND_FILENAME)
    elif x == 'l':
        winsound.PlaySound('l_morse_code', winsound.SND_FILENAME)


def filter_morse_list(list_to_filter: list) -> list:
    for index in range(len(list_to_filter)):
        if index+1 == len(list_to_filter) - 1:
            break
        else:
            if list_to_filter[index + 1].isspace() and list_to_filter[index] == 'l':
                del list_to_filter[index]
    del list_to_filter[len(list_to_filter) - 1]

    return list_to_filter


def morse_list_creator(morse_list: list) -> list:
    morse_code = []

    for element in morse_list:
        for index in range(len(element)):
            if index == len(element)-1 and element[index] != ' ':
                morse_code.append(element[index])
                morse_code.append('l')
            else:
                morse_code.append(element[index])
    if len(morse_code) > 1:
        filter_morse_list(morse_code)

    return morse_code


def __morse_decoder(message: str):
    morse_code = morse_list_creator(string_to_list(message))

    for character in morse_code:
        play_sound(character)


__morse_decoder("sos")
