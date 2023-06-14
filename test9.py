from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(url)
browser.execute_script("window.scrollBy(0, 100);")

button = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
button.click()

browser.execute_script("window.scrollBy(0, 100);")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)

button2 = browser.find_element(By.ID, 'solve').click()
print(browser.switch_to.alert.text.split()[-1])

alert = browser.switch_to.alert
alert.accept()

#vgbhj

browser.quit()

#vbnk