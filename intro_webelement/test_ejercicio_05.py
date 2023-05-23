import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demoqa.com/select-menu"

class TestLandingPage:

    #Para que abra el navegador en cada prueba
    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_old_style_select(self):
        #Seleccionar green de old style select menu
        time.sleep(5)
        menu_oldstyle = self.driver.find_element(By.XPATH, '//select[@id="oldSelectMenu"]')
        menu_oldstyle.click()
        select = Select(menu_oldstyle)
        select.select_by_value("2")
        assert select.first_selected_option.text == "Green"
        time.sleep(5)

