from selenium import webdriver
import time, threading

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/aim')

driver.implicitly_wait(5)

while True:
    try:
        driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-1k4dpwl e6yfngs0']/div/div[@class='css-q4kt6s e6yfngs1']/div[@class='css-z6vxiy e6yfngs3'][3]").click()
    except:
        pass
