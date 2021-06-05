import json
from selenium import webdriver

url = 'https://www.baidu.com'
d = webdriver.Firefox()
d.implicitly_wait(10)
d.get(url)
d.find_element_by_id('kw').send_keys('python')
d.find_element_by_id('su').click()
divs = d.find_elements_by_xpath('//div[@id="content_left"]/div[position()>1 and position() <=11]')
records = []
for div in divs:
    title = div.find_elements_by_xpath('.//h3/a')[0].text
    addr = div.find_elements_by_xpath('.//h3/a')[0].get_attribute('href')
    record = {'title': title, 'url': addr}
    records.append(record)
open('baidu_search_python.json', 'w').write(json.dumps(records))
d.quit()
