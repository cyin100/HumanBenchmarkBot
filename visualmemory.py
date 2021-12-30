from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from PIL import Image, ImageGrab
import pyautogui
import time

DESIRED_SCORE = 30 #Change to desired score, DEFAULT 30

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/memory')

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

gridIncrease = [0]
increment = 3
for i in range(30):
    for j in range(3):
        gridIncrease.append(gridIncrease[-1]+increment)
    increment += 2

score = 1
grid = 3

time.sleep(3)
driver.implicitly_wait(0)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='memory-test css-aix2he e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][2]/button[@class='css-de05nr e19owgy710']").click()

leftbound = 720
rightbound = 1209
topbound = 360
bottombound = 839

while score < DESIRED_SCORE:

    whitePixels = set()
    searching = True
    
    while searching:
        for i in range(1,grid):
            try:
                driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='memory-test css-aix2he e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div[@class='css-1qvtbrk e19owgy78']/div[@class='css-1qvtbrk e19owgy78'][2]/div[@class='css-hvbk5q eut2yre0']/div["+str(i)+"]/div[@class='active css-lxtdud eut2yre1']")
                time.sleep(0.7)

                screenshot = ImageGrab.grab()
                x = leftbound
                y = topbound
                while x < rightbound:
                    while y < bottombound:
                        if screenshot.getpixel((x, y)) == (255, 255, 255):
                            whitePixels.add(Pixel(x, y))
                        y += (bottombound-topbound)/grid
                    y = topbound
                    x += (rightbound-leftbound)/grid

                time.sleep(1)    
                for pixel in whitePixels:
                    pyautogui.click(x=pixel.x, y=pixel.y)
                    time.sleep(.01)
                
                searching = False

            except NoSuchElementException:
                pass

    score += 1

    for critPoint in gridIncrease:
        if(score == critPoint):
            grid += 1



