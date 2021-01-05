# binary/hexadecimal/octal to decimal converter and back


# ------------- BINARY CONVERTERS -------------


def binary_to_decimal(binary_string: str) -> str:
    multiplier = 0
    decimal_output = 0

    for number in binary_string[::-1]:
        if number in ['0', '1']:
            decimal_output += int(number) * 2**multiplier
            multiplier += 1
        else:
            return "wrong number"
    return str(decimal_output)


def decimal_to_binary(decimal_string: str) -> str:
    binary_output = ''

    if decimal_string.isdigit():
        decimal_int = int(decimal_string)

        while decimal_int >= 1:
            if decimal_int % 2 == 1:
                decimal_int -= 1
                binary_output += '1'
            else:
                binary_output += '0'
            decimal_int /= 2
    else:
        return "wrong number"

    return binary_output[::-1]


# ------------- HEX CONVERTERS -------------


def hex_to_decimal(hex_string: str) -> str:
    hex_accept = "0123456789ABCDEF"
    multiplier = 0
    hex_int = 0

    for number in hex_string[::-1]:
        if number in hex_accept:
            if number.isdigit():
                hex_int += int(number) * 16**multiplier
            else:
                hex_int += (ord(number) - 55) * 16**multiplier
            multiplier += 1
        else:
            return "wrong number"
    return str(hex_int)


def decimal_to_hex(decimal_string: str) -> str:
    hex_output = ''
    decimal_int = int(decimal_string)

    if decimal_string.isdigit():
        while decimal_int > 0:
            reminder = decimal_int % 16
            if reminder in range(0, 10):
                hex_output += str(reminder)
            else:
                hex_output += chr(reminder + 55)
            decimal_int = decimal_int // 16
    else:
        return "wrong number"
    return hex_output[::-1]


# ------------- OCTAL CONVERTERS -------------


def octal_to_decimal(octal_string: str) -> str:
    multiplier = 0
    decimal_output = 0

    for number in octal_string[::-1]:
        if int(number) in range(0, 8):
            decimal_output += int(number) * 8**multiplier
            multiplier += 1
        else:
            return "wrong number"
    return str(decimal_output)


def decimal_to_octal(decimal_string: str) -> str:
    octal_output = ''
    decimal_int = int(decimal_string)

    if decimal_string.isdigit():
        while decimal_int > 0:
            reminder = decimal_int % 8
            octal_output += str(reminder)
            decimal_int = decimal_int // 8
    else:
        return "wrong number"
    return octal_output[::-1]


# ------------- OTHER CONVERTERS -------------


def binary_to_hex(binary_string: str) -> str:
    return decimal_to_hex(binary_to_decimal(binary_string))


def hex_to_binary(hex_string: str) -> str:
    return decimal_to_binary(hex_to_decimal(hex_string))


def octal_to_hex(octal_string: str) -> str:
    return decimal_to_hex(octal_to_decimal(octal_string))


def hex_to_octal(hex_string: str) -> str:
    return decimal_to_octal(hex_to_decimal(hex_string))


def binary_to_octal(binary_string: str) -> str:
    return decimal_to_octal(binary_to_decimal(binary_string))


def octal_to_binary(octal_string: str) -> str:
    return decimal_to_binary(octal_to_decimal(octal_string))

