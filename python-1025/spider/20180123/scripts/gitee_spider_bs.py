import sys
import os
import json

import requests
from bs4 import BeautifulSoup as BS
from bs4.element import Tag


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
        s = BS(r.text, 'lxml')
        div = s('div', id="git-discover-list")[0]
        divs = [c for c in div.contents if c.name == 'div']
        for div in divs:
            url = div('div', class_="project-title")[0].a['href']
            url = '/'.join(url.split('/')[:2])
            url = url_prefix + url
            yield url

        try:
            next_url = s('a', rel="next")[-1]['href']
        except IndexError:
            next_url = ''
        if not next_url:
            break
        page_url = url_prefix + next_url


def extract_user_info(url):
    r = get_page(url)
    if r is None:       # 有些帐号不让访问，比如说某些公司帐号
        return

    s = BS(r.text, 'lxml')
    try:
        user_nick = s('a', class_="git-user-name-link")[0].text
    except IndexError:  # 遇到公司帐号时这里会出错，忽略公司帐号
        return

    user_name = url.split('/')[-1]
    divs = s('div', class_="git-user-infodata")
    divs2 = []
    for div in divs:
        a_set = div('a')
        for a in a_set:
            divs2.extend([c for c in a.contents if c.name == 'div'])
    nums = [div.text for div in divs2]
    nums = [int(n.strip()) for n in nums]
    followers, stars, following, watches = nums
    bios = s('div', class_="git-user-bio")
    user_desc = [x.text for x in bios[0]('span')][0].strip()
    join_time = [x.text for x in bios[-1]('span')][-1].strip()
    user_extra_info = '; '.join(
            [[d.text for d in b.descendants if isinstance(d, Tag)][-1] for b in bios[1:-1]]
        )

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
