import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://finance.yahoo.com/news"
response=requests.get(url)

print("response.ok : {} , response.status_code : {}".format(response.ok , response.status_code))
print("Preview of response.text : ", response.text[:500])

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception('Failed to load page {}'.format(url))
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc

#function call 
doc = get_page(url)

#appropritae tags common to news-headlines to filter out the necessary information.
a_tags = doc.find_all('a', {'class': "js-content-viewer"})
print(len(a_tags))

#print(a_tags[1])
news_list = []

#print top 10 Headlines
for i in range(1,len(a_tags)+1):
    news = a_tags[i-1].text
    news_list.append(news)
    print("Headline "+str(i)+ ":" + news)
news_df = pd.DataFrame(news_list)
#news_df.to_csv('Market_News')
print(news_df)