from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup

from crawler.utils.parsing import get_dict_from_dl


__all__ = (
    'album_search_from_melon',
)


def album_search_from_melon(request):
    keyword = request.GET.get('keyword')
    context = {}
    if keyword:

        album_info_list = []
        url = 'https://www.melon.com/album/detail.htm'
        params = {
            'q': keyword,
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text)
        for info in soup.select_one('div.section_info'):
            entry = info.select_one('div.entry')
            src = info.select_one('div.thumb img').get('src')

            title = entry.select_one('div.info > .song_name').contents[2].strip()
            url_img_cover = re.search(r'(.*?)/melon/quality.*', src).group(1)
            meta_dict = get_dict_from_dl(entry.select_one('div.meta dl'))

            album_info_list.append({
                'title': title,
                'url_img_cover': url_img_cover,
                'meta_dic': meta_dict,
            })
            context['album_info_list'] = album_info_list
        return render(request, 'album/album_search_from_melon.html', context)
