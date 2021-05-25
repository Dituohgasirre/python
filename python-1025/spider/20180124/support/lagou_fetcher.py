import os
import sys
import requests


def fetch(url):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "www.lagou.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }
    timeout = 10
    session = requests.Session()
    session.headers.update(headers)
    r = session.get(url, timeout=timeout)
    if r.status_code == 200:
        return r.text


if __name__ == '__main__':
    #
    # https://www.lagou.com/jobs/300010.html
    #
    if len(sys.argv) != 2:
        print('usage: %s url' % os.path.basename(sys.argv[0]))
        exit(1)

    url = sys.argv[1]
    text = fetch(url)
    if text:
        bname = os.path.basename(url)
        with open(bname, 'w') as f:
            f.write(text)
    else:
        print('no text')
