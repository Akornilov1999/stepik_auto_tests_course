'''Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "label > #input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(str(y))
    input2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckBox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    input3.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла