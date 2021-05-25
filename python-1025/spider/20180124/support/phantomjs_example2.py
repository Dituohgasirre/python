import sys
from selenium import webdriver

if len(sys.argv) < 2:
    print('date required')
    exit(1)

d = webdriver.PhantomJS()
dates = sys.argv[1:]
amount = 16
desc = 'testing'
url = 'http://localhost:8000/income/add/chenchenxing/'

for date in dates:

    d.get(url)

    # set the date
    e = d.find_element_by_id('id_earn_date')
    e.clear()
    e.send_keys(date)

    # set the total
    e = d.find_element_by_id('id_award_amount')
    e.clear()
    e.send_keys(amount)

    # set the desc
    e = d.find_element_by_id('id_award_desc')
    e.clear()
    e.send_keys(desc)

    # submit
    e = d.find_element_by_css_selector('input[type=submit]')
    e.click()

    print('done', date)
