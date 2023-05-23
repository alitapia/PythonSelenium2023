from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_desktops(self):
        # Variables de valor esperado
        exp_desktop_title = "iMac"
        exp_cart_value = "1 item(s) - $122.00"

        # Click desktops
        desktop_menu = self.driver.find_element(By.LINK_TEXT, "Desktops")
        assert desktop_menu.is_displayed() and desktop_menu.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        desktop_menu.click()

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


    def teardown_method(self):
        self.driver.quit()