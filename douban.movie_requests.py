import requests, json
from bs4 import BeautifulSoup

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

url_hot='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
url_highrate = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'
response = requests.get(url_highrate, headers=hds[1])
# print(response.text)
data = json.loads(response.text);
items = data['subjects']
for item in items[:]:
    print(item["title"] + ' ' + item['url'])
    if False:
        movie_resp = requests.get(item['url'], headers=hds[0])
        #print(movie_resp.text);
        soup = BeautifulSoup(movie_resp.text, 'html.parser')
        div = soup.select('strong.ll.rating_num')[0]
        print(div.text)