# Roman Number Generator (roman -> arabic)


roman_numbers = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


def arabic_to_roman(number: int) -> str:
    roman_output = []
    arabic_string = str(number)[::-1]
    power_counter = 0

    for digit in arabic_string:
        multiplier = 10**power_counter
        if int(digit) < 4:
            roman_output.append(int(digit) * roman_numbers[1*multiplier])
        elif int(digit) == 4:
            roman_output.append(roman_numbers[4*multiplier])
        elif int(digit) < 9:
            roman_output.append(roman_numbers[5*multiplier] + (int(digit)-5) * roman_numbers[1*multiplier])
        else:
            roman_output.append(roman_numbers[9*multiplier])
        power_counter += 1
    roman_output = list(filter(lambda x: x != "", roman_output[::-1]))

    return ''.join(roman_output)


print(arabic_to_roman(1995))
