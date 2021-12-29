from selenium import webdriver
import time, threading

DESIRED_SCORE = 1000

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/verbal-memory')

driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='verbal-memory-test ready e1uk74hg0 css-1o221zp e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][4]/button[@class='css-de05nr e19owgy710']").click()

seen = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='verbal-memory-test prompt e1uk74hg0 css-1o221zp e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][3]/button[@class='css-de05nr e19owgy710'][1]")
new = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='verbal-memory-test prompt e1uk74hg0 css-1o221zp e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][3]/button[@class='css-de05nr e19owgy710'][2]")
word = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='verbal-memory-test prompt e1uk74hg0 css-1o221zp e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][2]/div[@class='word']")

score = ""
set = set()

while score != "Score | "+str(DESIRED_SCORE-1):
    score = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='verbal-memory-test prompt e1uk74hg0 css-1o221zp e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='anim-slide-fade-in']/div/div[@class='css-1qvtbrk e19owgy78'][1]/p/span[@class='item score']").text.strip()
    newWord = word.text.strip()
    if newWord in set:
        seen.click()
    else:
        new.click()
        set.add(newWord)