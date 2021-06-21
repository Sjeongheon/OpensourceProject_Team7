from WebCrawling_TIMES import *
from summarization import TextRank
from nTokenizer import *
from papagoAPI import *

nTokenizer = nTokenizer()
TextRank = TextRank(nTokenizer)

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
	for d in data:	
		for t in d['text']:
			summarizedtext.append(TextRank.summarize(t,3))			
			translatedtext.append(translate(summarizedtext[-1]))
		d['summarizedtext'] = summarizedtext	
		d['translatedtext'] = translatedtext
	return data

