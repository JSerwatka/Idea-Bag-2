# Count Vowels
# mozna dodadac wypisywanie ile razy jaka sie litera pojawia i na jakich indeksach


def count_vowels(text):
    vowel_dic = {
        "a": [[], 0],
        "e": [[], 0],
        "i": [[], 0],
        "o": [[], 0],
        "u": [[], 0],
        "y": [[], 0]
    }

    for index in range(len(text)):
        if text[index].lower() == "a":
            vowel_dic["a"][0].append(index)
            vowel_dic["a"][1] += 1
        elif text[index].lower() == "e":
            vowel_dic["e"][0].append(index)
            vowel_dic["e"][1] += 1
        elif text[index].lower() == "i":
            vowel_dic["i"][0].append(index)
            vowel_dic["i"][1] += 1
        elif text[index].lower() == "o":
            vowel_dic["o"][0].append(index)
            vowel_dic["o"][1] += 1
        elif text[index].lower() == "u":
            vowel_dic["u"][0].append(index)
            vowel_dic["u"][1] += 1
        elif text[index].lower() == "y":
            vowel_dic["y"][0].append(index)
            vowel_dic["y"][1] += 1

    return vowel_dic


print(count_vowels("abcdeeouUuuiy"))