from urllib import request

from bs4 import BeautifulSoup


# keyword = request.GET.get('keyword')

keyword = '아이유'
url = 'http://www.melon.com/search/artist/index.htm'
params = {
    'q': keyword,
}
response = request.get(url, params)
soup = BeautifulSoup(response.text, 'lxml')

li_list = soup.select('div.list_atist12 > ul > li')

result =[]
for li in li_list:
     artist_id_a = li.select_one('dt a').get('href melon.link.goArtistDetail')
     # artist_id = artist_id_a.search(r"\('(\d+)").group(1)
     artist = li.select_one('dt a').text

     result.append(artist_id_a)