import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"

class TestLandingPage:

    #Para que abra el navegador en cada prueba
    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)
    #pruebas
    def test_search_field(self):
        time.sleep(5)
        # Click courses
        search_field = self.driver.find_element(By.XPATH, '//div[@class="input-group"]//input[@name="search"]')
        assert search_field.is_displayed(), "Campo de busqueda tiene que ser visible"
        assert search_field.is_enabled(), "Campo de busqueda tiene que estar habilitado"
        search_field.click()

        # Validate course page
        time.sleep(5)
        assert self.driver.current_url == "https://laboratorio.qaminds.com/", "URL tiene que ser la de lab"
        assert search_field.is_displayed(), "Campo de busqueda tiene que ser visible"
        assert search_field.is_enabled(), "Campo de busqueda tiene que estar habilitado"
        search_field.click()
        search_field.send_keys("iphone")
        search_btn = self.driver.find_element(By.XPATH, '//span[@class="input-group-btn"]//button')
        search_btn.click()
        time.sleep(5)
        iphone_img = self.driver.find_element(By.XPATH, '// img[ @ alt = "iPhone"]')
        assert iphone_img.is_displayed(), "Imagen del iPhone es visible confirmando la busqueda"



    #Cierra navegador
    def teardown_method(self):
        self.driver.quit()

