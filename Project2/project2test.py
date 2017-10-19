import unittest
import requests
import re
from bs4 import BeautifulSoup

def find_urls(s):
	ls = list()
	s = s.rstrip()
	ls = ls + re.findall('http://\S+\.\S\S*', s)
	ls = ls + re.findall('https://\S+\.\S\S*', s)
	return(ls)

def main():
	print(find_urls("http://www.google.com is a great site"))
	print(find_urls("I love looking at websites like http://etsy.com and http://instagram.com and lol.com and stuff"))
	print(find_urls("I love looking at websites like http://etsy and http://instagram.com and https://www.bbc.co.uk and stuff"))
	print(find_urls("the internet is awesome #worldwideweb"))
	print(find_urls("http://.c"))
	print(3)

if __name__ == '__main__':
	main()
