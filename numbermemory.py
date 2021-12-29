from selenium import webdriver
import time, threading
from pynput.keyboard import Key, Controller

DESIRED_SCORE = 20

keyboard = Controller()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/number-memory')

driver.implicitly_wait(DESIRED_SCORE*5/6)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='number-memory-test splash e12yaanm0 css-18qa6we e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][3]/button[@class='css-de05nr e19owgy710']").click()

while True:
    number = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='number-memory-test question e12yaanm0 css-18qa6we e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='big-number ']")
    newNumber = number.text.strip()

    driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='number-memory-test prompt e12yaanm0 css-18qa6we e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/form/div[@class='css-1qvtbrk e19owgy78'][2]/input").click()
    keyboard.type(newNumber)
    keyboard.press(Key.enter)

    driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='number-memory-test anim-correct e12yaanm0 css-18qa6we e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div[@class='showanswer']/div[2]/button[@class='css-de05nr e19owgy710']").click()
    