#!/usr/bin/python3

import requests

def get_translate(text):
	client_id = "S9r6V5c4xWp7xROMhlwd"
	client_secret = "ljwj9z9ayZ"

	data = {'text' : text,
		'source' : 'en',
		'target' : 'ko'}

	url = "https://openapi.naver.com/v1/papago/n2mt"

	header = {"X-Naver-Client-Id":client_id,
		  "X-Naver-Client-Secret":client_secret}

	response = requests.post(url, headers=header, data=data)
	rescode = response.status_code

	if(rescode==200):
		send_data = response.json()
		trans_data = (send_data['message']['result']['translatedText'])
		return trans_data
	else:
		print("Error Code:" , rescode)


trans = get_translate("Naver")
print(trans)

