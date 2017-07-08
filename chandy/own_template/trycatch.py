import requests
from bs4 import BeautifulSoup
r = requests.get('https://docs.google.com/forms/d/e/1FAIpQLSdwDrwgqZ1N6uFiMf1kxg3RcmhrSZ8mzQ8JPyYVlkL4xM8wyw/viewform')

r.text

soup = BeautifulSoup(r.text, 'html.parser')
form = soup.find('form')
inputs = form.find_all('input')
for i in inputs:
    if i['type'] != 'hidden':
        print i['aria-label']
        inputs[inputs.index(i)]['name'] = 'blah'
print [(element['name'], element['value']) for element in form.find_all('input')]
