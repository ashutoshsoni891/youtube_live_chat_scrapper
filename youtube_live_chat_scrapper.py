import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
browser=webdriver.Chrome(options = chromeOptions, executable_path = r'/home/aashutosh/Documents/webScrapingStuffs/chr webdriver/chromedriver')
time.sleep(4)

i =0
comments = []
while True:
    try:
        browser.get('https://www.youtube.com/watch?v=smZRzehsXHA')
        time.sleep(1)
        browser.switch_to.frame(browser.find_element_by_css_selector('iframe[id*="chatframe"]'))
        result = browser.find_elements_by_xpath('//*[@id="message"]')
        for r in result:
            print(str(i) + ' ' +r.text)
            comments.append(r.text)
            i=i+1
#     print('loop ended-----------------------------------------')
        df = pd.DataFrame(comments)
        df.to_csv('comments2.csv' , mode = 'a' , header = False)
        browser.switch_to.default_content()
    except exception as e:
        pass
    
    
