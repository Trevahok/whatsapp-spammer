from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

web = webdriver.Chrome(os.getcwd() + '/chromedriver')
web.get('http://web.whatsapp.com')
name=input('enter the victim name:')
message=input('enter ur message:')
times=int(input('enter the number of times u want me to send this:'))
try:
    ck=web.find_element_by_xpath('//*[@title="{}"]'.format(name))
    ck.click()
    textfield=web.find_elements_by_class_name("_2S1VP")
    for i in range(times):
        textfield[0].send_keys(message+Keys.ENTER)
except Exception as e:
    print(e)
web.close()
