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
        exp_no_elements_msg = "There are no products to list in this category."
        # Seleccionar la opcion de windows
        laptops_notebooks_menu = self.driver.find_element(By.XPATH, '//a[contains(@href,"category&path=18") and @class="dropdown-toggle"]')
        windows_menu = self.driver.find_element(By.XPATH, '//a[contains(@href,"category&path=18_45")]')

        assert laptops_notebooks_menu.is_displayed(), "Menu laptops and notebooks tiene que ser visible"
        laptops_notebooks_menu.click()
        assert windows_menu.is_enabled(), "Menu Windows tiene que estar habilitado"
        windows_menu.click()



        # Validate message no elements available
        time.sleep(5)
        no_elements_msg = self.driver.find_element(By.XPATH, '// div[ @ id = "content"] // p')
        assert no_elements_msg.is_enabled(), "Mensaje  debe ser visible"
        assert exp_no_elements_msg in no_elements_msg.text, f"Mensaje de confirmacion debe ser {exp_no_elements_msg}"

        #Validate Continue button
        continue_btn = self.driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
        assert continue_btn.is_enabled(),"Boton debe ser visible"
        continue_btn.click()

        #Validate return to home page
        time.sleep(5)
        assert self.driver.current_url == "https://laboratorio.qaminds.com/index.php?route=common/home", "URL tiene que ser la de lab"

    #Cierra navegador
    def teardown_method(self):
        self.driver.quit()