'''Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element(By.CSS_SELECTOR, "label > #input_value")
    x = x_element.text
    y = calc(x)

    element = browser.find_element(By.CSS_SELECTOR, "#answer")
    element.send_keys(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла