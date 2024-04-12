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
    # line = soup.find_all('tr')
    # print(soup.get_text())
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # print(soup.get_text())
    with open('data.csv', 'w', newline='') as file:  # open csv file
        field_names = ['Rank', 'State', 'Code', 'Population']  # field names
        writer = csv.DictWriter(file, fieldnames=field_names)  # open a writer
        list = []  # list of dictionaries with each state
        for state in soup.find_all('tr'):  # each state
            state_info = []  # list of info for each state
            for part in state:  # for each piece in state
                state_info.append(part.text)  # add it to the list
            list.append({'Rank': state_info[0], 'State': state_info[1], 'Code': state_info[2], 'Population': state_info[3]})  # put each state into a dictionary and add it to list of states
        # print(list)
        writer.writeheader()  # write the header
        for row in list:  # write it over to the csv file
            writer.writerow({'Rank': row['Rank'], 'State': row['State'], 'Code': row['Code'], 'Population': row['Population'],})
    file.close()

if __name__ == "__main__":
    main()