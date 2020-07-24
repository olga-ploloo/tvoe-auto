
import json
from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by/audi/a3/4508770')
    bt_elem = driver.find_elements_by_class_name('vehicle-form__parameter-item')
    bt_elem_text = []
    for elem in bt_elem:
        bt_elem_text.append(elem.text)
    #bt_data = bt_elem.text

    with open('json.json', 'w') as f:
        f.write(json.dumps(bt_elem_text))



if __name__== "__main__":
    main()