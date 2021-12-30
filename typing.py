from selenium import webdriver
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/typing')
driver.implicitly_wait(5)

while True:
    try:
        letter = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='e1q0za6r0 css-1c2t4mr e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only css-1qvtbrk e19owgy78'][1]/div[@class='letters notranslate']/span[@class='incomplete current']")
        key = letter.text.strip()
        if(key == ""):
            keyboard.press(Key.space)
        else:
            keyboard.press(key)
    except:
        break
    