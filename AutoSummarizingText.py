
import requests
from bs4 import BeautifulSoup


def getTextfromPost(url):
	print('Getting your post')
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "lxml")
	text = ' '.join(map(lambda p : p.text, soup.find_all('article')))
	text = text.encode('ascii', errors='replace').replace(b"?", b" ").decode('ascii')
	return text

print(getTextfromPost('https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/'))