
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict


def getTextfromPost(url):
	print('Getting your post')
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "lxml")
	text = ' '.join(map(lambda p : p.text, soup.find_all('article')))
	text = text.encode('ascii', errors='replace').replace(b"?", b" ").decode('ascii')
	return text


def summarize(text, n):
	print('Summarizing your post')
	sents = sent_tokenize(text)
	assert n <= len(sents)
	word_sent = word_tokenize(text.lower())
	_stopwords = set(stopwords.words('english') + list(punctuation))

	word_sent = [word for word in word_sent if word not in _stopwords]
	freq = FreqDist(word_sent)

	ranking = defaultdict(int)

	for i, sent in enumerate(sents):
		for w in word_tokenize(sent.lower()):
			if w in freq:
				ranking[i] += freq[w]

	sents_idx = nlargest(n, ranking, key=ranking.get)
	return [sents[j] for j in sorted(sents_idx)]


if __name__ =="__main__":
	url = 'https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new'\
		  '-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/'
	text = getTextfromPost(url)
	summary = summarize(text, 4)
	print(summary)