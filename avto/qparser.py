import csv

from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by/audi/a3/4508770')
    bt_elem = driver.find_elements_by_class_name('vehicle-form__parameter-item')
    #cash_elem = driver.find_element_by_class_name('vehicle-form__price vehicle-form__price_condensed')
    bt_elem_text = []
    for elem in bt_elem:
        elem = elem.text
        bt_elem_text.append(elem.replace('\n', ':'))
    #bt_data = bt_elem.text

    myFile = open('csv0.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        for row in bt_elem_text:
            line = row.split(',')
            writer.writerow(line)
            print(line)
        #writer.writerow(cash_elem.text)
        #writer.writerow(bt_data)

    #requiredHtml = driver.page_source


    #print(driver.page_source)
    print(bt_elem_text)

if __name__== "__main__":
    main()