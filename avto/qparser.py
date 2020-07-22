from selenium import webdriver

def main():
    chrome_driver = '/home/bobik/projects/tvoe_auto/avto/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    driver.get('https://ab.onliner.by')
    bt_elem = driver.find_element_by_class_name('vehicle-form__offers')


    #print(driver.page_source)
    print(bt_elem.text)

if __name__== "__main__":
    main()