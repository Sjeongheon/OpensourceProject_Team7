import requests
from bs4 import BeautifulSoup
import time 
from random import randint
def WebCrawler_TIMES(subject) :
	session = requests.Session()
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
	}
	html = session.get("https://www.nytimes.com/section/" + subject, headers=headers).content
	soup_main = BeautifulSoup(html, 'html.parser')
	spliter = '"'
	latest_titlepath = "html body div div main section div div section div ol li div div a h2"
	latest_title_textpath = "html body div div main section div div section div ol li div div a p"
	latest_titlesourcepath = "html body div div main section div div section div ol li div div a"
	text_path = "html body div div div div main div article section div div p"
	title1 = soup_main.select(latest_titlepath)[0].get_text()
	title2 = soup_main.select(latest_titlepath)[1].get_text()
	title3 = soup_main.select(latest_titlepath)[2].get_text()

	title_text1 = soup_main.select(latest_title_textpath)[0].get_text()
	title_text2 = soup_main.select(latest_title_textpath)[1].get_text()
	title_text3 = soup_main.select(latest_title_textpath)[2].get_text()
	
	title_sources = soup_main.find_all('li',class_= "css-ye6x8s",limit=3)
	title_imgs = []
	titleURLs = []
	for source in title_sources:
		imgsource = source.find('img')
		if imgsource is None:
			title_imgs.append("No main image included")
		else:
			title_imgs.append(imgsource.attrs.get('src'))
		
	for i in range(3):
		titleURLsource = soup_main.select(latest_titlesourcepath)[i+1]
		if title_sources[i].find('a',class_="css-1d32glx") is None:
			titleURLs.append("https://www.nytimes.com/"+titleURLsource.attrs.get('href'))
		else:
			titleURLs.append(title_sources[i].find('a',class_="css-1d32glx").attrs.get('href'))
	print(titleURLs)
	
	MAX_Sleep_Time = 3
	soups = []
	for i in range(3):
		latest_page = session.get(titleURLs[i], headers=headers)
		time.sleep(randint(1, MAX_Sleep_Time))
		soups.append(BeautifulSoup(latest_page.content, 'html.parser'))

	pages = []
	imgs = []
	dates = []
	for soup in soups:
		page = ""
		source = soup.select(text_path)
		img = soup.find('img')
		timesource = soup.find('time')
		for text in source:
			page += text.get_text()
		if img is None:
			img = 'No main image included'
		else :
			img = img.attrs.get('src')
		if timesource is None:
			date = 'Unknown Time Data'
		else:
			date = timesource.get_text()
		pages.append(page)
		imgs.append(img)
		dates.append(date)

	title = [title1,title2,title3]
	title_texts = [title_text1,title_text2,title_text3]	
	newsinfdic = {'text' : pages,
			   'title' : title,
			   'title_text' : title_texts,
			   'title_img' : title_imgs,
			   'img' : imgs,
			   'date' : dates}

	return newsinfdic
