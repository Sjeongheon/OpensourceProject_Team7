#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import sys
import urllib.request
client_id = "S9r6V5c4xWp7xROMhlwd"
client_secret = "ljwj9z9ayZ"
encText = urllib.parse.quote("Pleas enter the sentence")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
	response_body = response.read()
	print(response_body.decode('utf-8'))
else:
	print("Error Code:" + rescode)



