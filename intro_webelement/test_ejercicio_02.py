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
    def test_search_tablets(self):
        time.sleep(5)
        #Variables de valor esperado
        exp_title = "Samsung Galaxy Tab 10.1"
        exp_cost = "$241.99"
        exp_wish_list_label = "1"
        exp_success_msg = "Success: You have added"

        # Click tablets
        tablets_menu = self.driver.find_element(By.XPATH, '//a[contains(@href, "category&path=57")]')
        assert tablets_menu.is_displayed(), "Menu tiene que ser visible"
        assert tablets_menu.is_enabled(), "Menu tiene que estar habilitado"
        tablets_menu.click()

        # Validate title
        time.sleep(5)
        tablets_title = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href, 'product_id=49')]")
        assert tablets_title.is_displayed(), "Titulo tiene que ser visible"
        assert tablets_title.text == exp_title, f"Titulo tiene que ser{exp_title}"

        #Click titulo
        tablets_title.click()

        #Valida costo
        cost = self.driver.find_element(By.XPATH, "//div[@id='content']//li//h2")
        assert cost.is_displayed(), "Costo debe ser visible"
        assert cost.text == exp_cost, f"Costo debe ser {exp_cost}"

        # Agregar wish list
        wish_list = self.driver.find_element(By.XPATH, '//div[@id="content"]//button[./i[@class="fa fa-heart"]]')
        assert wish_list.is_displayed() , "Wish list debe ser visible"
        assert wish_list.is_enabled(), "Wish list debe estar habilitado"
        wish_list.click()

        # Validar wish list
        wish_list_label = self.driver.find_element(By.XPATH, '//a[@id="wishlist-total"]/span')
        assert wish_list_label.is_displayed(), "Wish list label debe ser visible"
        assert exp_wish_list_label in wish_list_label.text, f"Wish list label debe tener {exp_wish_list_label}"

        # Agregarlo al carro de compra
        add_to_cart = self.driver.find_element(By.ID, "button-cart")
        assert add_to_cart.is_displayed() and add_to_cart.is_enabled(), "Agregar a carrito debe estar visible"
        add_to_cart.click()

        success_msg = self.driver.find_element(By.CLASS_NAME, "alert-success")
        assert success_msg.is_enabled(), "Mensaje confirmacion debe ser visible"
        print(success_msg.text)
        assert exp_success_msg in success_msg.text, f"Mensaje de confirmacion debe ser {exp_success_msg}"

    #Cierra navegador
    def teardown_method(self):
        self.driver.quit()