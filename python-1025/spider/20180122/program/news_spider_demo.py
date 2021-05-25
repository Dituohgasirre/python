import re
from pprint import pprint

import requests


def get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text.encode('latin-1').decode('gbk')
        return html


def formalize(urls, url):
    protocol = url.split(':')[0]
    prefix = '/'.join(url.split('/')[:3])
    res = []
    for u in urls:
        if u.startswith('//'):
            res.append(protocol + ':' + u)
        elif u.startswith('/'):
            res.append(prefix + u)
    return res


def extract_news_data(url):
    html = get_page(url)
    title = re.findall('<h1 .*>(.*)</h1>', html, flags=re.DOTALL)[0].strip()
    time = re.findall(r'<span id="pubtime_baidu">(.*?)</span>',
                      html, flags=re.DOTALL)[0]
    source = re.findall(r'<span id="source_baidu">.*?<a .*?>(.*?)</a></span>',
                        html, flags=re.DOTALL)[0]
    return dict(title=title, time=time, source=source, url=url)


def extract_urls(url):
    html = get_page(url)
    pat = r"""<div class="xwzxdd-dbt">.*?href=['"]([^'"]+)"""
    urls = re.findall(pat, html, flags=re.DOTALL)
    urls = formalize(urls, url)
    return urls


if __name__ == '__main__':
    start_url = 'http://www.chinanews.com/'
    urls = extract_urls(start_url)
    records = [extract_news_data(url) for url in urls]
    pprint(records)
