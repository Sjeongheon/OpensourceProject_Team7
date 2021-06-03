import requests
from bs4 import BeautifulSoup

def WebCrawler_TIMES(subject) :
    page = requests.get("https://www.nytimes.com/section/" + subject)
    soup = BeautifulSoup(page.content, 'html.parser')
    spliter = '"'
    latest_titletextPath = "html body div div main section div div section div ol li div div a"
    latest_titlepath = "html body div div main section div div section div ol li div div a h2"
    #latest_imgpath = "html body div div main section div div section div ol lidiv div a div figure div" - later implementation
    title1 = soup.select(latest_titlepath)[0].get_text()
    title2 = soup.select(latest_titlepath)[1].get_text()
    title3 = soup.select(latest_titlepath)[2].get_text()

    titletext1 = str(soup.select(latest_titletextPath)[1])
    titletext2 = str(soup.select(latest_titletextPath)[2])
    titletext3 = str(soup.select(latest_titletextPath)[3])

    titleURL1 = titletext1.split(spliter)[1]
    titleURL2 = titletext2.split(spliter)[1]
    titleURL3 = titletext3.split(spliter)[1]
    latest1_page = requests.get("https://www.nytimes.com" + titleURL1)
    latest2_page = requests.get("https://www.nytimes.com" + titleURL2)
    latest3_page = requests.get("https://www.nytimes.com" + titleURL3)
    soup1 = BeautifulSoup(latest1_page.content, 'html.parser')
    soup2 = BeautifulSoup(latest2_page.content, 'html.parser')
    soup3 = BeautifulSoup(latest3_page.content, 'html.parser')
    source1 = soup1.find('main', id = "site-content").get_text()
    source2 = soup2.find('main', id = "site-content").get_text()
    source3 = soup3.find('main', id = "site-content").get_text()
    newsinfdic = {'latest1_text' : source1,
                  'latest2_text' : source2,
                  'latest3_text' : source3,
                  'latest1_title' : title1,
                  'latest2_title' : title2,
                  'latest3_title' : title3}
    return newsinfdic
