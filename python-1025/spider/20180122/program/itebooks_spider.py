import os
import sys
import re
import json

import requests


def get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text


def get_detail_url(isbn):
    search_url = 'http://it-ebooks.info/search/?type=isbn&q=%s' % isbn
    html = get_page(search_url)
    if html is not None:
        url = re.findall('<a href="(/book[^"]+)"', html)[0]
        prefix = '/'.join(search_url.split('/')[:3])
        url = prefix + url
        return url


def fetch(pat, html):
    x = re.findall(pat, html)
    if x:
        return x[0]


def extract_detail_info(url):
    html = get_page(url)
    res = {}
    if html is not None:
        res['publisher'] = fetch(r'itemprop="publisher">(.*?)</a>', html)
        res['author'] = fetch(r'itemprop="author"[^>]*?>(.*?)</b>', html)
        res['year'] = fetch(r'itemprop="datePublished">(.*?)</b>', html)
        res['pages'] = fetch(r'itemprop="numberOfPages">(.*?)</b>', html)
        res['language'] = fetch(r'itemprop="inLanguage">(.*?)</b>', html)
        res['id'] = int(url.split('/')[-2])
        return res


def merge_info(record, extra):
    record = {k.lower(): v for k, v in record.items()}
    record.update(extra)
    return record


def save(record, output):
    output.write(json.dumps(record) + '\n')
    output.flush()


def collect_basic_info(keyword):
    fmt = 'http://it-ebooks-api.info/v1/search/%s/page/%s'
    count = 0
    page = 1
    while True:
        url = fmt % (keyword, page)
        text = get_page(url)
        if text:
            try:
                result = json.loads(text)
            except json.decoder.JSONDecodeError:
                ...
            else:
                if result['Error'] == '0':
                    books = result['Books']
                    print('collected page %s/%s' % (page, int(result['Total'])//10))
                    yield books
                    count += 10     # 每页显示10条记录
                    if count >= int(result['Total']):
                        break
        page += 1


def collect_extra_info(books):
    for book in books:
        isbn = book['isbn']
        detail_url = get_detail_url(isbn)
        if not detail_url:
            print('can not get detail url of isbn: %s' % isbn)
            continue
        extra_info = extract_detail_info(detail_url)
        if not extra_info:
            print('can not get detail info: %s' % detail_url)
            continue
        extra_info['url'] = detail_url
        book = merge_info(book, extra_info)
        yield book


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: %s keyword output-file' % os.path.basename(sys.argv[0]))
        exit(1)

    keyword = sys.argv[1]
    output = open(sys.argv[2], 'w')

    all_books = collect_basic_info(keyword)     # 生成器，返回一组书的概要信息
    for books in all_books:
        for book in collect_extra_info(books):  # 生成器，返回一本书的详情
            save(book, output)
            print('fetched book <isbn: %s>' % book['isbn'], flush=True)
