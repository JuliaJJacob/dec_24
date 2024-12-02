import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options # для управления настройками запуска браузера

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')  # безголовый режим
    browser = webdriver.Firefox(options=options) # открываем браузер
    browser.maximize_window() # разворачиваем окно
    browser.implicitly_wait(3) # ждем подгрузки элементов, неявное ожидание
    yield browser
    browser.close()