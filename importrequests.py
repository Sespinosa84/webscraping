import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink') # grap the links
votes = soup.select('.score') #grap the votes 

def create_custom_hn(links, votes):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		#hn.append(title)
		href = links[idx].get('href', None)
		hn.append({'title', title,'link', href})

	return hn 


print(create_custom_hn(links, votes))
  
