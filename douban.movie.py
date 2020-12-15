from requests_html import HTMLSession, AsyncHTMLSession
# import nest_asyncio

# nest_asyncio.apply()


url = 'https://movie.douban.com/'
header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
session = HTMLSession()
r = session.get(url = url, headers=header)

for url in r.html.links:
    if url.find('subject') != -1:
        print(url)





