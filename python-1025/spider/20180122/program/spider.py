# 十九、用python写一个网页归档程序（爬虫），把 http://quotes.toscrape.com/ 网站上的10个页面全部下载
# 下来。从起始地址 http://quotes.toscrape.com/ 开始，把余下的9个页面的地址找出来，然后爬取。

import re
import requests


def download(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r
    else:
        print('failed to download %s (%s)' % (url, r.status_code))


def parse(r):
    m = re.findall(r'<a href="(/page/[0-9]+/)">Next', r.text)
    if m:
        next_url = m[0]
    else:
        next_url = None
    return (r.text, next_url)


def save(data, r):
    num = r.url.split('/')[-2]
    fname = 'page-%s.html' % num
    open(fname, 'w').write(data)


def engine(start_url):
    urls = [start_url]

    for url in urls:
        print('processing %s' % url)
        r = download(url)
        if r is not None:
            data, next_url = parse(r)
            save(data, r)
            if next_url is not None:
                abs_url = urljoin(r, next_url)
                urls.append(abs_url)


def urljoin(r, url):
    if url.startswith('http'):
        return url
    base = '/'.join(r.url.split('/')[:3])
    return base + url


if __name__ == '__main__':
    url = 'http://quotes.toscrape.com/'
    engine(url)
