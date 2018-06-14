import bs4
import requests
import pandas as pd

url = "http://planetpython.org"
source = requests.get(url)
#print(source)

soup = bs4.BeautifulSoup(source.content, 'lxml')
#print(soup)
soup_array = []
for link in soup.find_all('a'):
	data = link.get('href')
	soup_array.append(data)
print(soup_array)
#df = pd.DataFrame(soup_array)
#print(df)
#df.to_csv('test.csv')