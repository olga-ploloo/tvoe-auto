import csv

from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by')
    bt_elem = driver.find_element_by_class_name('vehicle-form__offers')
    bt_data = bt_elem.text
    myFile = open('csv_data.csv1', 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=' ')
        writer.writerows(map(lambda x: [x], bt_data))
    #requiredHtml = driver.page_source


    #print(driver.page_source)
    print(bt_elem)

if __name__== "__main__":
    main()