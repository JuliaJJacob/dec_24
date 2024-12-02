
from selenium.webdriver.common.by import By # импорт способов поиска элементов в браузере
import time

# далее импорт из наших классов
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    # browser.get('https://www.demoblaze.com/index.html') #конкретная ссылка
    # galaxy_s6 = browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]') # сохраняем найденный элемент в переменную
    # galaxy_s6.click()
    product_page = ProductPage()
    product_page.check_title_is('Samsung galaxy s6')
    # title = browser.find_element(By.CSS_SELECTOR, value='h2')
    # assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    # browser.get('https://www.demoblaze.com/index.html')
    homepage.click_monitor()
    # monitors_link = browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    # monitors_link.click()
    time.sleep(5) # BAD!
    homepage.products_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, value='.card') # возвращает список элементов
    # assert len(monitors) == 2 # длина списка

