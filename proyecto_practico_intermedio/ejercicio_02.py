
from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_display(self, validate_cinema=None):
        # Variables de valor esperado
        exp_error_no_product_msg = 'There is no product that matches the search criteria.'
        exp_product_title_cinema = 'Apple Cinema 30"'
        id_cinema = "42"
        exp_product_title_nano = 'iPod Nano'
        id_nano = "36"
        exp_product_title_touch = 'iPod Touch'
        id_touch = "32"
        exp_product_title_mac = 'MacBook Pro'
        id_macpro = "45"

        # Busqueda Display
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='button']//i[@class='fa fa-search']")
        assert search_button.is_displayed() and search_button.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_button.click()
        no_product_msg = self.driver.find_element(By.XPATH, "//div[@id='content']/p[text()='There is no product that matches the search criteria.']")
        assert exp_error_no_product_msg in no_product_msg.text

        # search in descriptions
        description_checkbox = self.driver.find_element(By.XPATH, "//input[@id='description']")
        description_checkbox.click()
        search_button_secondary = self.driver.find_element(By.XPATH, "//input[@id='button-search']")
        search_button_secondary.click()

        # Validate function
        def validate_product(productid: str, expected_value: str):
            current_value = self.driver.find_element(By.XPATH, f"//div[@class='caption']//a[contains(@href,'product_id={productid}')]")
            return current_value.text


        # validate displayed products
        result = validate_product(id_cinema, exp_product_title_cinema)
        assert result == exp_product_title_cinema
        result = validate_product(id_nano, exp_product_title_nano)
        assert result == exp_product_title_nano
        result = validate_product(id_touch, exp_product_title_touch)
        assert result == exp_product_title_touch
        result = validate_product(id_macpro, exp_product_title_mac)
        assert result == exp_product_title_mac

    def teardown_method(self):
        self.driver.quit()
