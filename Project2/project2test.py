import unittest
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

def find_urls(s):
	ls = list()
	s = s.rstrip()
	ls = ls + re.findall('http://\S+\.\S\S*', s)
	ls = ls + re.findall('https://\S+\.\S\S*', s)
	return(ls)


def get_umsi_data():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    pages = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    names = dict()
    jobs = list()
    for page in pages:
        url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page='+ page
        html = requests.get(url, headers= {'User-Agent': 'SI_CLASS'})
        soup = BeautifulSoup(html.text, 'html.parser')
        tags = soup('div')
        l = list()
        for tag in tags:
        	if(tag.attrs == {'class': ['field-item', 'even']}):
        		l.append(tag.text)
        l = [ x for x in l if "\n" not in x ]
        jobs.extend(l)
    return(jobs)
    #for page in pages:
    #    url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page='+ page
    #    html = requests.get(url, headers= {'User-Agent': 'SI_CLASS'})
    #    soup = BeautifulSoup(html.text, 'html.parser')
    #Your code here
    #    tags = soup.find_all('h2')
    #    d = dict()
    #    for tag in tags:
    #        if(tag.attrs == {}):
    #            d[tag.text] = ""
    #    names.update(d)

def main():
	print(find_urls("http://www.google.com is a great site"))
	print(find_urls("I love looking at websites like http://etsy.com and http://instagram.com and lol.com and stuff"))
	print(find_urls("I love looking at websites like http://etsy and http://instagram.com and https://www.bbc.co.uk and stuff"))
	print(find_urls("the internet is awesome #worldwideweb"))
	print(find_urls("http://.c"))
	print(get_umsi_data())
if __name__ == '__main__':
	main()

