import requests
from bs4 import BeautifulSoup
import random

class MakeForm():
    def generate(self,url):
        form_id = ""
        for i in range(5):
            form_id += str(random.choice(range(0,10)))
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        form = soup.find_all('form')
        form_generated = "<form method=\"get\" action=\"form_validate\">"
        form_generated += "<input type=\"hidden\" name=\"form_id\" value=\""+str(form_id)+"\">"
        txtno = 0
        lbno = 0
        rdno = 0
        return_id_userd = []
        for i in form:
            form_contents = []
            inputs = i.find_all('input')
            for i in inputs:
                form_element = {}
                if i['type'] == 'text':
                    form_element['name'] = i['aria-label']
                    form_generated += '<input type="text" placeholder="'+form_element['name']+'" name="text'+str(txtno)+'" id ="'+form_element['name'].lower()+'">'
                    return_id_userd.append('text'+str(txtno))
                    txtno += 1
            for pic in soup.find_all('div'):
                if pic.get('role', 'n/a') == 'listbox':
                    print "listbox"
                    list_box_items = []
                    for pic1 in pic.find_all('div'):
                        if pic1.get('aria-label', 'n/a') != 'n/a':
                            print pic1.get('aria-label', 'n/a')
                            list_box_items.append(pic1.get('aria-label', 'n/a'))
                    form_generated +='<select name="listbox'+str(lbno)+'" >'
                    return_id_userd.append('listbox'+str(lbno))
                    lbno += 1
                    for lst_item in list_box_items:
                        form_generated +='<option value="'+ lst_item +'">'+ lst_item +'</option>'
                    form_generated +="</select>"

                if pic.get('role', 'n/a') == 'radiogroup':
                    print "listbox"
                    list_box_items = []
                    for pic1 in pic.find_all('div'):
                        if pic1.get('aria-label', 'n/a') != 'n/a':
                            print pic1.get('aria-label', 'n/a')
                            list_box_items.append(pic1.get('aria-label', 'n/a'))

                    for lst_item in list_box_items:
                        form_generated +='<input type="radio" name="radio'+str(rdno)+'" value="'+lst_item+'" checked> '+ lst_item + '<br>'
                    return_id_userd.append('radio'+str(rdno))
                    rdno += 1
        form_generated +='<input type="submit">'
        form_generated +='</form>'
        return form_generated,form_id,return_id_userd

# unit test
# m = MakeForm()
# form_generated,form_id = m.generate('https://docs.google.com/forms/d/e/1FAIpQLSdwDrwgqZ1N6uFiMf1kxg3RcmhrSZ8mzQ8JPyYVlkL4xM8wyw/viewform')
