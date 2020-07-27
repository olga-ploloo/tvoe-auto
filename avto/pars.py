import csv
import time

from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by/?page=1')
    time.sleep(15)
    name = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_title']")
    years = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_year']")
    price = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_price']")
    motor = driver.find_elements_by_xpath("//div[@class='vehicle-form__description vehicle-form__description_base vehicle-form__description_primary vehicle-form__description_engine vehicle-form__description_condensed-other']")
    text_name = elem_to_text(name)
    text_years = elem_to_text(years)
    text_price = elem_to_text(price)
    text_motor = elem_to_text(motor)
    with open('csv01.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i[0] for i in bt_elem_text])
        writer.writerow([i[1] for i in bt_elem_text])

def elem_to_text(stri):
    text = []
    for elem in stri:
        elem = elem.text
        text.append(elem)
    return text



if __name__== "__main__":
    main()