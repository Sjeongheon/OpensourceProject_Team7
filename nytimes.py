#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

def get_soup_obj(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	return soup

for sid in ["world", "us", "politics"]:
	sec_url = "https://www.nytimes.com/section/" + sid
	print("section url : ", sec_url)

	soup = get_soup_obj(sec_url)

	lis3 = soup.find('ol', aria-live='off').find_all("li", limit=3)
	for li in lis3:
		news_info = {
			"title" : li.h2.attrs.get('class'),
			"date" : li.find(class="css-n1vcs8 e1xfvim33").text,
		

	
