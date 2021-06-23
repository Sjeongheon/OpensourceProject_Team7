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

def integrationFuction(time):
	a = True	
	today = time
	subject1 = "world"
	subject2 = "science"
	subject3 = "health"
	subjects = [subject1,subject2,subject3]
	es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)		
	try:	
		allinf = es.search(index = subjects[0],doc_type = today)['hits']['hits']
		if not allinf:
			a = False
	except :
		a = True	
	
	if a :
		dic1 = WebCrawler_TIMES(subject1)
		dic2 = WebCrawler_TIMES(subject2)
		dic3 = WebCrawler_TIMES(subject3)
		#crawling
		translatedtext = []
		summarizedtext = []
		data = [dic1,dic2,dic3]
		summarized_text_length = 6
		for d in data:
			for t in d['text']:
				summarizedtext.append(TextRank.summarize(t,summarized_text_length))			
				translatedtext.append(translate(summarizedtext[-1]))
			d['summarizedtext'] = summarizedtext	
			d['translatedtext'] = translatedtext
		
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
				titlehash = hash(data[i]['title'][j])
				try:	
					allinf = es.search(index = subjects[0])['hits']['hits']
					for inf in allinf:
						if e["title"] == inf['_source']['title']:
							a = False				
							break
				except :
					a = True
				
				if a:
					es.index(index = subjects[i], doc_type = today, body = e)
	






