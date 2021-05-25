import os
import sys
import json
import time
from selenium import webdriver


def login(url, username, password):
    old_url = d.current_url
    d.get(url)
    d.find_element_by_id('id_username').send_keys(username)
    d.find_element_by_id('id_password').send_keys(password)
    d.find_element_by_id('id_password').submit()
    time.sleep(1)
    if d.current_url != old_url:
        return True
    else:
        return False


def get_target_urls(data_url):
    d.get(data_url)
    a_set = d.find_elements_by_xpath('//tbody//a')
    urls = [a.get_attribute('href') for a in a_set]
    return urls


def extract_target_info(url):
    d.get(url)
    name = d.find_element_by_id('id_name').get_attribute('value')
    age = d.find_element_by_id('id_age').get_attribute('value')
    create_date = d.find_element_by_id('id_create_0').get_attribute('value')
    create_time = d.find_element_by_id('id_create_1').get_attribute('value')
    record = {'name': name, 'age': age, 'create': '%s %s' % (create_date, create_time)}
    return record


def save(record, outfile):
    text = json.dumps(record)
    outfile.write(text + '\n')
    outfile.flush()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: %s out-file' % os.path.basename(sys.argv[0]))
        exit(1)

    outfile = open(sys.argv[1], 'w')
    login_url = 'http://localhost:8000/admin/'
    data_url = 'http://localhost:8000/admin/contact/contact/'
    username = 'admin'
    password = 'abcd/1234'
    # os.environ['MOZ_HEADLESS'] = '1'
    d = webdriver.Firefox()
    d.implicitly_wait(10)

    print('login...')
    if login(login_url, username, password):
        print('fetching urls...')
        urls = get_target_urls(data_url)
        for url in urls:
            print('extracting data of %s' % url)
            record = extract_target_info(url)
            save(record, outfile)
    d.quit()
