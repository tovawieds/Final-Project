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
    # print(soup.prettify())
    # for state in soup.find_all('tr'):
    #     print(state)
    #     for part in state:
    #         print(part.text)
    line = soup.find_all('tr')
    # print(soup.get_text())
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # print(soup.get_text())
    with open('data.csv', 'w', newline='') as file:  # open csv file
        field_names = ['Rank', 'State', 'Code', 'Population']  # field name
        writer = csv.DictWriter(file, fieldnames=field_names)  # open a writer
        list = []
        for state in soup.find_all('tr'):  # extract the url's and titles
            state_info = []
            for part in state:
                state_info.append(part.text)
            list.append({'Rank': state_info[0], 'State': state_info[1], 'Code': state_info[2], 'Population': state_info[3]})
        print(list)
        writer.writeheader()  # write the header
        for row in list:  # write it over to the csv file
            writer.writerow({'Rank': row['Rank'], 'State': row['State'], 'Code': row['Code'], 'Population': row['Population'],})
    file.close()

if __name__ == "__main__":
    main()