# In Order

def check_if_sorted(string: str) -> str:
    words = string.split()

    for element in words:
        if element == "".join(sorted(element)):
            print(element + " - in order", end = " ")
        else:
            print(element + " - not in order", end = " ")


check_if_sorted("biopsy billowy chef")