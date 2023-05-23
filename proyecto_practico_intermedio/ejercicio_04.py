from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_samsung(self):
        # Variables de valor esperado
        exp_default_currency = "$"
        # exp_cart_value = "1 item(s) - $122.00"

        # Validate default currency
        default_currency = self.driver.find_element(By.XPATH, "//form[@id='form-currency']//strong")
        assert default_currency.text == exp_default_currency

        # Search samsung product
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Samsung")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='button']//i[@class='fa fa-search']")
        assert search_button.is_displayed() and search_button.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_button.click()


        #Select Samsung SyncMaster
        select_syncmaster = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=33')]")
        select_syncmaster.click()
        value_dolars = self.driver.find_element(By.XPATH, "//li//h2")
        dolar_price = value_dolars.text
        dolar_price_amount = dolar_price[1:]

        change_currency_button = self.driver.find_element(By.XPATH, "//form[@id='form-currency']//span")
        change_currency_button.click()

        euro_button = self.driver.find_element(By.XPATH, "//button[@name='EUR']")
        euro_button.click()

        value_euros = self.driver.find_element(By.XPATH, "//li/h2")
        euro_price = value_euros.text
        euro_price_amount = euro_price[:-1]


        #Validate euro price < dolar price
        assert euro_price_amount < dolar_price_amount



        '''
        # click on mac option on desktop menu
        mac_option = self.driver.find_element(By.XPATH, "//a[contains(@href,'category&path=20_27')]")
        mac_option.click()

        # Validate product displayed
        mac_title = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=41')]")
        assert mac_title.text == exp_desktop_title

        # Open product
        mac_title.click()

        #Add to cart

        add_cart_button = self.driver.find_element(By.XPATH, "//div[@class='form-group']/button[@id='button-cart']")
        add_cart_button.click()

        # Validate cart is updated
        cart_value = self.driver.find_element(By.XPATH, "//span[@id='cart-total']")
        assert exp_cart_value == cart_value.text

'''
    def teardown_method(self):
        self.driver.quit()