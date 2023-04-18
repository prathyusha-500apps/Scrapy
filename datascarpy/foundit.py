import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    templete = 'https://www.foundit.in/srp/results?{}&{}'
    url = templete.format(position, location)
    url = get_url('Accountant', 'Hyderabad / Secunderabad, Telangana, ')
    responce = requests.get('url')
    soup = BeautifulSoup(responce.content, 'html.parser')
    card = soup.find_all('div', 'cardContainer activeCard')
    return url


def get_record(card):
    atag = card.h3.a
    job_title =atag.get('title')
    job_url ='https://www.foundit' + atag.get('href')
    company =card.find('div','companyName')
    job_location = card.find('title',)
    post_date = card.find('p','timeText')
    today = datetime.today().strftime('%y-%m-%d')
    try:
        job_salary = card.find('span', 'salarytext').text.strip()
    except AttributeError:
        job_salary = ''
    record = (job_title , job_url , company , job_location , post_date , today , job_salary ) 

    return record

def main(position, location):
    records = []
    url = get_url(position, location)

    #extract the job data
    while True:
        responce = requests.get('url')
        soup = BeautifulSoup(responce.content, 'html.parser')
        cards = soup.find_all('div', 'cardContainer activeCard')

        for card in cards:
            record = get_record(card)
            record.append(record)

        try:
            url = 'https://www.foundit' + soup.find('div', 'arrow arrow-right disabled').get('href')
        except AttributeError:
            break

#save the job data
    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['jobtitle', 'joburl', 'company', 'joblocation', 'postdate', 'today', 'salary'])
        writer.writerows(records)
