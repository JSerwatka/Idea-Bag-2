# Count words in a String
'''
todo:
    1. zamienić tę wersję programu na maszynę stanów, aby był bardziej
    odporny na wielokrotne spacje
    2. program nie liczy paragrafów, naprawić
'''


def count_words(string: str) -> str:
    words_counter = 1
    paragraph_counter = 1

    if type(string) is str:
        for sign in string:
            if sign.isspace():
                words_counter += 1
            elif sign == "\n" or sign == "\r":
                paragraph_counter += 1
    else:
        return "This is not a string"

    return "Strig has {} words and {} paragraphs".format(words_counter, paragraph_counter)


print(count_words("Nazywam się Jakub Serwatka i jestem absolwentem AGH \n"
                  "fsdfdsfsdf\n"
                  "fsdf\n"
                  "sdf"))
