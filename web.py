import re
import sys
import csv
import requests
from bs4 import BeautifulSoup


def main():
    scrape("https://www.statsamerica.org/sip/rank_list.aspx?rank_label=pop1")


def scrape(s):
    html = requests.get(s)
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup.find_all('tr'))
    print(soup.get_text())
    with open('data.csv', 'w', newline='') as file:  # open csv file
        field_names = ['Rank', 'State', 'Code', 'Population']  # field name
        writer = csv.DictWriter(file, fieldnames=field_names)  # open a writer
        list = []
        for link in soup.find_all('tr'):  # extract the url's and titles
            list.append({'Rank': link.get('td'), 'State': link.get('td'), 'Code': link.get('td'), 'Population': link.get('td')})
        writer.writeheader()  # write the header
        for row in list:  # write it over to the csv file
            writer.writerow({'Rank': row['Rank'], 'State': row['State'], 'Code': row['Code'], 'Population': row['Population'],})
    file.close()

if __name__ == "__main__":
    main()