# Get atomic time from internet clock
# todo: naprawić brak polskich znaków, zroić, aby parsing nie odbywał się w pętli
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_current_atomic_time():
    # variables
    country = 'poland'
    records = []

    # ---> scraping country's clock <---
    r = requests.get('https://www.timeanddate.com/worldclock/' + country)
    soup = BeautifulSoup(r.text, 'html.parser')

    # getting table of cities of the country
    cities_table_html = soup.find('table', {'class': 'zebra fw tb-wc zebra'}).contents[1:]

    # ---> getting city and current time <---
    for line in cities_table_html:
        lines = line.find_all('td')
        # every other tag in lines
        elements = list((i for i in lines if lines.index(i) % 2 != 1))[:-2]
        # main scraping of cities and time
        for element in elements:
            name_of_the_city = element.a.text

            # parsing time
            r = requests.get('https://www.timeanddate.com' + element.a['href'])
            soup = BeautifulSoup(r.text, 'html.parser')
            main_part_html = soup.find('div', {'id': 'qlook'}, {'class': 'three columns tc'})
            # date and time
            date = main_part_html.p.text
            time = main_part_html.find('span', {'id': 'ct'}, {'class': 'h1'}).text[:-3]
            records.append((name_of_the_city, date, time))

    # ---> creating database <---
    df = pd.DataFrame(records, columns=['city', 'date', 'time'])
    df.to_csv('time_in_the_city.csv', index=False, encoding='utf-8')


get_current_atomic_time()
