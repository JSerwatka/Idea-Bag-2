# Kaprekar numbers
# todo: dodanie możliwości szukania tych liczb w innych podstawach - binarny, haxadecymalny, itp.


def split_n_add(number: int) -> bool:
    number_str = str(number**2)
    digit_stack = ""

    for i in range(0, len(number_str)):
        if i == len(number_str)-1:
            return False
        elif int(number_str[i+1:]) == 0:
            return False
        else:
            digit_stack += number_str[i]
            if int(digit_stack) + int(number_str[i+1:]) == number:
                return True


def main():
    while True:
        print("In what range should I look for Kaprekar's numbers \n")
        range_low = int(input("Minimum: "))
        range_max = int(input("Maximum: ")) + 1

        if range_low >= range_max or range_low <= 0 or range_max <= 0:
            print("Error: wrong range")
            continue
        for number in range(range_low, range_max):
            if number == 1:
                print("1 is a Kaprekar's number")
            elif split_n_add(number):
                print("%d is a Kaprekar's number" % number)
        break

main()




