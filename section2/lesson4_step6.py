'''Какую ошибку вы увидите в консоли,
если попытаетесь выполнить команду browser.find_element(By.ID, "button")
после открытия страницы http://suninjuly.github.io/cats.html?'''

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла