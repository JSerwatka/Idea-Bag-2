# Roman to Arabic numeral converter
'''todo:
 1. Nie pozwolić aby liczba jak VIIIII była akceptowana
 2. Nie pozwolić aby liczba jak IXIX była akceptowana
 3. Nie pozwolić aby liczba XCM była akceptowana
'''


roman_numbers = {
    '0': 0,
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

def test_if_roman(digit_prev, digit_new) -> bool:
    if roman_numbers[digit_prev] < roman_numbers[digit_new] and digit_prev + digit_new not in roman_numbers:
        return False
    elif digit_new not in roman_numbers:
        return False
    else:
        return True


def roman_to_arabic(number: str) -> int or str:
    arabic_number = 0
    digit_prev = '0'

    for digit in number:
        if test_if_roman(digit_prev, digit):
            if digit_prev + digit in roman_numbers:
                arabic_number += roman_numbers[digit_prev + digit] - roman_numbers[digit_prev]
            else:
                arabic_number += roman_numbers[digit]
            digit_prev = digit
        else:
            return "Wrong Roman"

    return arabic_number


print(test_if_roman("I","V"))