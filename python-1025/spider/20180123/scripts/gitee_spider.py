import sys
import os
import json

import requests
from lxml import etree


def get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r


def fetch_urls(page_url):
    url_prefix = '/'.join(page_url.split('/')[:3])

    while True:
        es = page_url.split('=')
        page_num = 1 if len(es) == 1 else int(es[-1])
        print('fetching page %s' % page_num)

        r = get_page(page_url)
        if r is None:
            break
        tree = etree.HTML(r.text)
        divs = tree.xpath('//div[@id="git-discover-list"]/div')
        for div in divs:
            url = div.xpath('.//div[@class="project-title"]/a/@href')[0]
            url = '/'.join(url.split('/')[:2])
            url = url_prefix + url
            yield url

        next_url = tree.xpath('//a[@rel="next" and text()="\n"]/@href')
        if not next_url:
            break
        page_url = url_prefix + next_url[0]


def extract_user_info(url):
    r = get_page(url)
    if r is None:       # 有些帐号不让访问，比如说某些公司帐号
        return

    tree = etree.HTML(r.text)
    try:
        user_nick = tree.xpath('//a[@class="git-user-name-link"]/text()')[0]
    except IndexError:  # 遇到公司帐号时这里会出错，忽略公司帐号
        return

    user_name = url.split('/')[-1]
    nums = tree.xpath('//div[@class="git-user-infodata"]//a/div/text()')
    nums = [int(n.strip()) for n in nums]
    followers, stars, following, watches = nums
    bios = tree.xpath('//div[@class="git-user-bio"]')
    user_desc = bios[0].xpath('.//span/text()')[0].strip()
    join_time = bios[-1].xpath('.//span/text()')[-1].strip()
    user_extra_info = '; '.join([b.xpath('.//*/text()')[-1] for b in bios[1:-1]])
    return {'user_nick': user_nick, 'user_name': user_name,
            'user_desc': user_desc, 'join_time': join_time,
            'followers': followers, 'stars': stars,
            'following': following, 'watches': watches,
            'user_extra_info': user_extra_info}


def save(record, output):
    output.write(json.dumps(record) + '\n')
    output.flush()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: %s output-file' % os.path.basename(sys.argv[0]))
        exit(1)

    output = open(sys.argv[1], 'w')
    start_url = 'https://gitee.com/explore/recommend?page=1'
    seen_urls = set()
    urls = fetch_urls(start_url)
    for url in urls:
        if url in seen_urls:
            print('--> url already seen: %s' % url)
            continue
        seen_urls.add(url)
        record = extract_user_info(url)
        if record is None:
            print('not scraped %s' % url)
            continue
        save(record, output)
        print('scraped user %s<%s>' % (record['user_nick'], record['user_name']))
