# CAESAR'S CIPHER


def encrypting(string: str, shift: int) -> str:
    encrypted_string = ''
    for letter in string:
        if letter.isspace():
            encrypted_string += ' '
        else:
            ascii_code = ord(letter)
            if ascii_code - shift < ord('A'):
                ascii_code = 91 - (ord('A') - (ascii_code - shift))
            else:
                ascii_code -= shift
            encrypted_string += chr(ascii_code)
    return encrypted_string


def decrypting(string: str, shift: int) -> str:
    decrypted_string = ''
    for letter in string:
        if letter.isspace():
            decrypted_string += ' '
        else:
            ascii_code = ord(letter)
            if ascii_code + shift > ord('Z'):
                ascii_code = 64 + abs(ord('Z') - (ascii_code + shift))
            else:
                ascii_code += shift
            decrypted_string += chr(ascii_code)
    return decrypted_string


def _caesars_cipher():
    string = input("String: ")
    shift = int(input("Shift: "))
    cipher_type = input("encrypt/decrypt (e/d): ")
    max_shift = ord('Z') - ord('A')
    string_correct = all((char.isupper() and char.isupper()) or char.isspace() for char in string)
    shift_correct = shift <= max_shift
    cipher_type_correct = cipher_type == 'e' or cipher_type == 'd'
    if not string_correct:
        return "Incorrect string"
    elif not shift_correct:
        return "Shift out of range"
    elif not cipher_type_correct:
        return "Wrong ciphering type"
    else:
        if cipher_type == 'e':
            return encrypting(string, shift)
        else:
            return decrypting(string, shift)



print(_caesars_cipher())
