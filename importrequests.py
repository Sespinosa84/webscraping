import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink') # grap the links
subtext = soup.select('.subtext') #grap the votes 

links2 = soup2.select('.storylink') # grap the links
subtext2 = soup2.select('.subtext') #grap the votes 

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		#hn.append(title)
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			score = int(vote[0].getText().replace(' points', ''))
			if score > 99:
				hn.append({'title': title, 'link': href, 'votes': score})

	return sort_stories_by_votes(hn) 


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
  
