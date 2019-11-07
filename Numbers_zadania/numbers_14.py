bils = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

cost = input("Cost of product: ")
paid = input("Client paid: ")

if cost.isalnum() and paid.isalnum():
    to_give = float(paid) - float(cost)

    for element in bils:
        print("nr of %s: %s" % (element, to_give//element))
        to_give -= element * (to_give // element)
else:
    print("error")

'''
    co więcej zrobić:
1. zabezpieeczyć przed wpisywaniem na input nie-stringu, który nie jest liczbą np. dsdsakj (ale bez cudzysłowia)
2. zebezpieczenie się przed wpisywaniem liczby o ponad 2 liczbach po przecinku

'''