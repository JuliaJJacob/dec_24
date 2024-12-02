from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitors_link = self.browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
        monitors_link.click()

    def products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, value='.card')  # возвращает список элементов
        assert len(monitors) == count