'''Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    x_element1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x_element2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(x_element1.text) + int(x_element2.text)
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла