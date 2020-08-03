import csv
import time
import pandas as pd
from selenium import webdriver


def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by/')
    page_count = len(driver.find_elements_by_xpath("//li[@class='vehicle-pagination__pages-item']"))
    print(page_count)
    for i in range(1, 3):
        driver.get('https://ab.onliner.by/?order=created_at%3Adesc&page='+str(i))
        time.sleep(5)
        name = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_title']")
        years = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_year']")
        price = driver.find_elements_by_xpath("//div[@class='vehicle-form__offers-part vehicle-form__offers-part_price']")
        text_name = elem_to_text(name)
        text_years = elem_to_text(years)
        price_bel, price_doll, price_euro = [], [], []
        for elem in price:
            elem = elem.text
            elem = (elem.replace('\n', '/')).split('/')
            price_bel.append((elem[0][:-3]).replace(' ', ''))
            price_doll.append((elem[1][:-3]).replace(' ', ''))
            price_euro.append((elem[2][1:-2]).replace(' ', ''))


        df = pd.DataFrame({"Title": text_name, "Bel": price_bel, "Dol": price_doll, "Euro": price_euro, "Year": text_years})
        df.to_csv("output1.csv", index=False, mode='a', header=False)

def elem_to_text(stri):
    text = []
    for elem in stri:
        elem = elem.text
        text.append(elem.replace('Обмен', ''))
    return text




if __name__== "__main__":
    main()