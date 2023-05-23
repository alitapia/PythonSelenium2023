from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)


    def test_search_display(self):
        # Variables de valor esperado
        exp_error_no_product_msg = 'There is no product that matches the search criteria.'
        exp_product_title_cinema = 'Apple Cinema 30"'
        exp_product_title_nano = "iPod Nano"
        exp_product_title_touch = "iPod Touch"
        exp_product_title_mac = "MacBook Pro"


        # Busqueda Display
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='button']//i[@class='fa fa-search']")
        assert search_button.is_displayed() and search_button.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_button.click()
        no_product_msg = self.driver.find_element(By.XPATH, "//div[@id='content']//='There is no product that matches the search criteria.']")
        assert exp_error_no_product_msg in no_product_msg.text
        #search in descriptions
        description_checkbox = self.driver.find_element(By.XPATH, "//input[@id='description']")
        description_checkbox.click()
        search_button_secondary = self.driver.find_element(By.XPATH, "//input[@id='button-search']")
        search_button_secondary.click()
        #validate displayed products
        cinema = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=42')]")
        assert cinema.text == exp_product_title_cinema
        nano = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=36')]")
        assert nano.text == exp_product_title_nano
        touch = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=32')]")
        assert touch.text == exp_product_title_touch
        mac = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=45')]")
        assert mac.text == exp_product_title_mac

    def teardown_method(self):
        self.driver.quit()