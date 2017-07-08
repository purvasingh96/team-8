import requests
from bs4 import BeautifulSoup
r = requests.get('https://docs.google.com/forms/d/e/1FAIpQLSdwDrwgqZ1N6uFiMf1kxg3RcmhrSZ8mzQ8JPyYVlkL4xM8wyw/viewform')

soup = BeautifulSoup(r.text, 'html.parser')
form = soup.find_all('form')
for i in form:
    print i.find_all('input')
    print i.find_all('select')

for i in form:
    print i

inputs = form.find_all('input')
inputs = form.find_all('select')
for i in inputs:
    if i['type'] != 'hidden':
        print i['aria-label'],i

print [(element['name'], element['value']) for element in form.find_all('input')]

import glob

ha = os.listdir('/Users/admin/Desktop/Search___Go_[v1.8]')
os.path
cwd = os.getcwd()
cwd
class ParseWebsite():
    def __init__(self,url,google=True):
        self.html = requests.get(url)
        soup = BeautifulSoup(self.html.text,'html.parser')
        form = soup.find('form')
        inputs = form.find_all('input')
        self.all_inputs = []
        for i in inputs:
            form_element = {}
            if i['type'] != 'hidden':
                if google:
                    form_element['name'] = i['aria-label']
                else:
                    try:
                        form_element['name'] = i['placeholder']
                    except Exception as e:
                        form_element['name'] = i['name']
                form_element['type'] = i['type']
                self.all_inputs.append(form_element)
    def make_form(self):
        string_generated = ""
        string_generated += '<form method="get" action="dynamically_decided">'
        for i in self.all_inputs:
            string_generated += i['name'] + '</br> <input name="ident' + i['name'] + '" type="' + i['type'] + '" placeholder="' + i['name'] + '">'
            string_generated += '</br>'
        string_generated += '<input type=submit value="next">'
        string_generated += "</form>"
        return string_generated


# Unit Tests

p = ParseWebsite('https://docs.google.com/forms/d/e/1FAIpQLSdwDrwgqZ1N6uFiMf1kxg3RcmhrSZ8mzQ8JPyYVlkL4xM8wyw/viewform')
p.make_form()
