import json 
import requests 
import bs4
import fake_headers 
from pprint import pprint 
headers_gen = fake_headers.Headers(browser='chrome', os='win') 
response = requests.get(url='https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_gen.generate())
html_data = response.text 
soup = bs4.BeautifulSoup(html_data, 'lxml') 
article_full = soup.find_all('div', class_='serp-item')
keywords = ['Flask', 'Django'] 
parsed_data = [] 
for article_tag in article_full: name_of_vacancy = article_tag.find('a').text 
# Название вакансии
href = article_tag.find('a', class_='serp-item__title')['href'] 
# Ссылка на вакансию
name_of_company = article_tag.find('a', class_='bloko-link bloko-link_kind-tertiary').text
 # Название компании 
name_of_city = article_tag.find('div', {'data-qa':'vacancy-serp__vacancy-address'}).text 
# Название города 
money = article_tag.find('span', class_='bloko-header-section-2') 
if money: money = money.text
else: money = 'Не указана'
parsed_href = requests.get(url=href, headers=headers_gen.generate()) 
html_parsed_href = parsed_href.text 
if 'Django' or 'Flask' in html_parsed_href: parsed_data.append({ "Название вакансии": name_of_vacancy, "Ссылка на вакансию": href, "Название компании": name_of_company, "Название города": name_of_city, "Зарплата": money}) 
with open('parsed_vacancies1.json', 'w', encoding='utf-8') as file: json.dump(parsed_data, file, ensure_ascii=False) 
pprint(parsed_data)