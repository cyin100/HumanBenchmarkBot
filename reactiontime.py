from selenium import webdriver
import time, threading

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/reactiontime')

driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='view-splash e18o0sx0 css-saet2v e19owgy77']/div[@class='css-42wpoy e19owgy79']").click()

while True:
    try:
        driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='view-go e18o0sx0 css-saet2v e19owgy77']/div[@class='css-42wpoy e19owgy79']").click()
        driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='view-result e18o0sx0 css-saet2v e19owgy77']/div[@class='css-42wpoy e19owgy79']").click()
    except:
        break
        