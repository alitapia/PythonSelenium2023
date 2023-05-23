import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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

    def test_standard_multi_select(self):
        #Seleccionar volvo y audi
        time.sleep(5)
        menu_standard_multi = self.driver.find_element(By.XPATH, '//select[@id="cars"]')
        #menu_standard_multi.click()
        select = Select(menu_standard_multi)
        #Select objSelect = new Select(driver.findElement(By.id(Element_ID)));
        select.select_by_value("volvo")
        select.select_by_value("audi")
        for option in select.all_selected_options:
            option: WebElement
            assert option.text == "Volvo" or option.text == "Audi"
        time.sleep(5)

