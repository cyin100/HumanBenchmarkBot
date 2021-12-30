from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from PIL import Image, ImageGrab
import pyautogui
import time

DESIRED_SCORE = 20 #Change to desired score, DEFAULT 20

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/sequence')

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

score = 1

time.sleep(3)
driver.implicitly_wait(0)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='memory-test ea4to4h0 css-1q5jb46 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][2]/button[@class='css-de05nr e19owgy710']").click()

leftbound = 770
rightbound = 1259
topbound = 410
bottombound = 889

while score < DESIRED_SCORE:

    whitePixels = []
    counter = 0
    
    while counter < score:
        screenshot = ImageGrab.grab()
        x = leftbound
        y = topbound
        while x < rightbound:
            while y < bottombound:
                if screenshot.getpixel((x, y)) == (255, 255, 255):
                    whitePixels.append(Pixel(x, y))
                    counter += 1
                    time.sleep(0.5)
                y += (bottombound-topbound)/3
            y = topbound
            x += (rightbound-leftbound)/3
    
    time.sleep(0)
    for pixel in whitePixels:
        pyautogui.click(x=pixel.x, y=pixel.y)
        time.sleep(.01)
    
    score += 1



