# Zip/Postal Code Lookup
import requests
import re
from bs4 import BeautifulSoup


def country_by_zip_code():
    # output list of cities
    list_of_cities_text = []

    # ---> getting and checking zip code <---
    pattern = r"^\d\d-\d\d\d$"
    entered_zip_code = input("Podaj kod pocztowy: ")
    # checking if zip code has proper format
    if not re.match(pattern, entered_zip_code):
        raise NameError("Invalid zip code format!")

    # ---> parsing site html <---
    r = requests.get("https://znajdzkodpocztowy.pl/szukaj/mk-" + entered_zip_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    main_text_html = soup.find('div', attrs={'class': "col-md-8"})

    # checking if zip code is in a database
    if main_text_html.find('div', attrs={'class': 'alert alert-danger'}):
        return main_text_html.find('div', attrs={'class': 'alert alert-danger'}).text

    else:
        list_of_cities_html = main_text_html.find_all('div', attrs={'class': 'row tab_tresc'})[2:]

        # checking the format of the response and iterating through it
        if list_of_cities_html[0].find('a'):
            for i in range(len(list_of_cities_html)):
                try:
                    list_of_cities_text.append(list_of_cities_html[i].find('a').text)
                except AttributeError:  # ruling out incorrectly formatted container
                    pass
        else:
            list_of_cities_text = [y.find('h2') for y in list_of_cities_html]

        # getting polish signs and forcing no to have duplicates in the list
        list_of_cities_unicode = set([x.encode('raw_unicode_escape').decode('utf-8') for x in list_of_cities_text])

        # ---> creating output message <---
        output_string = "Lista miast z kodem pocztowym " + entered_zip_code + ':\n'
        for element in list_of_cities_unicode:
            output_string += element + '\n'

        return output_string


print(country_by_zip_code())
