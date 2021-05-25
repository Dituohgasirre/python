import sys
import os
import json

import requests
from lxml import etree


def get_page(url):
    r = requests.get(url)
    if r.ok:
        return r.text


def extract_first(element, path):
    res = element.xpath(path)
    if res:
        return res[0]


def scrape_page(url):
    html = get_page(url)
    if html is not None:
        tree = etree.HTML(html)
        divs = tree.xpath('//div[@class="quote"]')
        for div in divs:
            text = extract_first(div, './/*[@itemprop="text"]/text()')
            author = extract_first(div, './/*[@itemprop="author"]/text()')
            tags = extract_first(div, './/*[@itemprop="keywords"]/@content')
            record = {'text': text, 'author': author, 'tags': tags}
            yield record

        next = extract_first(tree, '//li[@class="next"]/a/@href')
        if next:
            url_prefix = '/'.join(url.split('/')[:3])
            next = url_prefix + next
        else:
            next = ''
        yield next


def save(record, output):
    json_text = json.dumps(record)
    outfile.write(json_text + '\n')
    outfile.flush()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: %s out-file' % os.path.basename(sys.argv[0]))
        exit(1)

    outfile_path = sys.argv[1]
    outfile = open(outfile_path, 'w')
    next_url = 'http://quotes.toscrape.com/page/1/'

    while next_url:
        print('scraping page %s' % next_url)
        for item in scrape_page(next_url):
            if isinstance(item, str):
                next_url = item
            else:
                save(item, outfile)
