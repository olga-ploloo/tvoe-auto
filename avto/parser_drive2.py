import csv
import time
import pandas as pd
from selenium import webdriver

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://www.drive2.ru/cars/?all')
    name = driver.find_elements_by_xpath("//a[@class='c-link c-link--text']")
    text_name = elem_to_text(name)[:6]
    car_brand_list = [i.text.split('\n') for i in name]
    model_list = []
    print(text_name)
    for i in text_name:
        driver.get('https://www.drive2.ru/cars/' + i)
        model = driver.find_elements_by_xpath("//nav[@class='is-short c-makes c-makes--no-top-margin is-animated']")
        for i in model:
            model_list.append(i.text.split('\n'))
    with open('car_brend.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow('Brand'.split('\n'))
        for row in car_brand_list:
            writer.writerow(row)


    print(model_list, len(model_list))


def elem_to_text(stri):
    text = []
    for elem in stri:
        elem = elem.text
        if elem == 'Mercedes-Benz':
            text.append('mercedes')
        elif elem == 'Лада':
            text.append('lada')
        else:
            text.append(elem.lower().replace(' ', ''))
    return text

if __name__== "__main__":
    main()