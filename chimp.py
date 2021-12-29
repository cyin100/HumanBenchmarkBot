from selenium import webdriver
import time, threading

DESIRED_SCORE = 30

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://humanbenchmark.com/tests/chimp')

class Point:
    def __init__(self, number, i, j):
        self.number = number
        self.i = i
        self.j = j

points = []
score = 4
driver.implicitly_wait(0)
driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-1qvtbrk e19owgy78'][2]/button[@class='css-de05nr e19owgy710']").click()

while score < DESIRED_SCORE:
    for i in range(1, 6):
        for j in range(1, 9):
            try:
                number = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-gmuwbf']/div/div[@class='css-k008qs']["+str(i)+"]/div[@class='css-19b5rdt']["+str(j)+"]").text.strip()
                points.append(Point(int(number), i, j))
            except:
                break
    
    points = sorted(points, key=lambda point: point.number)

    for point in points:
        print(str(point.number)+" "+str(point.i)+" "+str(point.j))
        try:
            driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-gmuwbf']/div/div[@class='css-k008qs']["+str(point.i)+"]/div[@class='css-19b5rdt']["+str(point.j)+"]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-gmuwbf']/div/div[@class='css-k008qs']["+str(point.i)+"]/div[@class='css-10qtjsi']["+str(point.j)+"]").click()

        for index in range(len(points)):
            if points[index].i == point.i and points[index].j > point.j:
                points[index].j -= 1

    points.clear()
    driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='css-1gr1qbh']/div[4]/div[@class='css-12ibl39 e19owgy77']/div[@class='css-42wpoy e19owgy79']/div[@class='desktop-only']/div[@class='css-1qvtbrk e19owgy78'][3]/button[@class='css-de05nr e19owgy710']").click()
    score += 1
