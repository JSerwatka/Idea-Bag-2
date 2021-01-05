# Numbers of days xx/xx/xxxx
# Bez uwzględnienia roku przestępnego


long_months = ['01', '03', '05', '07', '08', '10', '12']


def format_check(string_1: str, string_2: str) -> bool:
    number_indexes = [0, 1, 3, 4, 6, 7, 8, 9]

    for element_1, element_2 in zip(string_1, string_2):
        if len(string_1) > 10 or len(string_2) > 10:
            return False
        elif string_1.index(element_1) in number_indexes:
            if not element_1.isdigit() or not element_2.isdigit():
                return False
        else:
            if element_1 != '/' or element_2 != '/':
                return False

    return True


def date_check(string_1: str, string_2: str) -> bool:
    strings = [string_1, string_2]

    if int(string_1[6:]) <= int(string_2[6:]):
        for string in strings:
            if int(string[3:5]) > 12:
                return False
            elif string_1[3:5] in long_months and int(string_1[0:2]) > 31:
                return False
            elif string_1[3:5] == '02' and int(string_1[0:2]) > 28:
                return False
            elif string_1[3:5] not in long_months and int(string_1[0:2]) > 30:
                return False

        return True
    else:
        return False


def months_to_days(month: str) -> int:
    days = 0
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    if month == '01':
        return days
    else:
        for i in months:
            if i == month:
                break
            else:
                if i in long_months:
                    days += 31
                elif i == '02':
                    days += 28
                else:
                    days += 30

    return days


def day_calculator(date_1: str, date_2: str) -> int or str:
    if not format_check(date_1, date_2) or not date_check(date_1, date_2):
        return "Wrong date format"
    else:
        date_1_sum = int(date_1[0:2]) + months_to_days(date_1[3:5]) + (int(date_1[6:])-1)*365
        date_2_sum = int(date_2[0:2]) + months_to_days(date_2[3:5]) + (int(date_2[6:])-1)*365
        return date_2_sum - date_1_sum


print(day_calculator("10/07/2012", "30/04/2015"))
