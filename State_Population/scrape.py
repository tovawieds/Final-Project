from flask import Flask, render_template, request, redirect, url_for
import os
import csv
import requests
from bs4 import BeautifulSoup



def main():  # main function to run the program
    scrape("https://www.statsamerica.org/sip/rank_list.aspx?rank_label=pop1")


def scrape(s):  # a method to scrape the data from the website and put it into a csv file
    html = requests.get(s)
    soup = BeautifulSoup(html.text, "html.parser")
    with open('data.csv', 'w', newline='') as file:  # open csv file
        field_names = ['Rank', 'State', 'Code', 'Population']  # field names
        writer = csv.DictWriter(file, fieldnames=field_names)  # open a writer
        list = []  # list of dictionaries with each state
        for state in soup.find_all('tr'):  # each state
            state_info = []  # list of info for each state
            for part in state:  # for each piece in state
                state_info.append(part.text)  # add it to the list
            state_info[3] = state_info[3].replace(",", "")  # remove all commas from number
            list.append({'Rank': state_info[0], 'State': state_info[1], 'Code': state_info[2], 'Population': state_info[3]})  # put each state into a dictionary and add it to list of states
        print(list)
        writer.writeheader()  # write the header
        for row in list:  # write it over to the csv file
            writer.writerow({'Rank': row['Rank'], 'State': row['State'], 'Code': row['Code'], 'Population': row['Population'],})
    file.close()



if __name__ == "__main__":
    main()