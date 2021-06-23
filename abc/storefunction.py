from WebCrawling_TIMES import *
from summarization import TextRank
from Tokenizer_ver1 import *
from papagoAPI import *
import sys
import time
from elasticsearch import Elasticsearch

es_host = "127.0.0.1"
es_port = "9200"
Tokenizer = Tokenizer()
TextRank = TextRank(Tokenizer)

def integrationFuction():
	subject1 = "world"
	subject2 = "science"
	subject3 = "health"
	dic1 = WebCrawler_TIMES(subject1)
	dic2 = WebCrawler_TIMES(subject2)
	dic3 = WebCrawler_TIMES(subject3)
	#crawling
	translatedtext = []
	summarizedtext = []
	data = [dic1,dic2,dic3]
	subjects = [subject1,subject2,subject3]
	for d in data:
		for t in d['text']:
			summarizedtext.append(TextRank.summarize(t,3))			
			translatedtext.append(translate(summarizedtext[-1]))
		d['summarizedtext'] = summarizedtext	
		d['translatedtext'] = translatedtext
	
	es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)
	
	for i in range(3):
		for j in range(3):		
			e = {
				"title":data[i]['title'][j],
				"title_text":data[i]['title_text'][j],
				"title_img":data[i]['title_img'][j],
				"date":data[i]['date'][j],	
				"img":data[i]['img'][j],
				"text":data[i]['text'][j],
				"summarizedtext":data[i]['summarizedtext'][j],
				"translatedtext":data[i]['translatedtext'][j]
			}
			today = time.ctime()
			titletext = str(data[i]['title'][j]).replace(",","").replace(" ","").lower()
			es.index(index = titletext ,doc_type = subjects[i], id = j, body = e) #title 
		






