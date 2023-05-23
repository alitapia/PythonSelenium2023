
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from factory.webdriver_factory import get_driver


URL = "https://demoqa.com/select-menu"

class TestLandingPage:
    #Para que abra el navegador en cada prueba
    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
    def test_old_style_select(self):
        #Seleccionar green de old style select menu
        menu_oldstyle = self.driver.find_element(By.XPATH, '//select[@id="oldSelectMenu"]')
        menu_oldstyle.click()
        select = Select(menu_oldstyle)
        select.select_by_value("2")
        assert select.first_selected_option.text == "Green"

    def teardown_method(self):
        self.driver.quit()