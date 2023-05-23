import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"

class TestLandingPage:

    #Para que abra el navegador en cada prueba
    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)
    #pruebas
    def test_login(self):
        time.sleep(5)
        #Variables de valor esperado
        usuario_input = "ali@test.com"
        password_input = "invalidpass"
        exp_error_login_msg = "Warning: No match for E-Mail Address and/or Password."

        mail_field = self.driver.find_element(By.XPATH, '//input[@id="input-email"]')
        pass_field = self.driver.find_element(By.XPATH, '//input[@id="input-password"]')

        #introduce mail
        assert mail_field.is_displayed() and mail_field.is_enabled(), "Campo Mail tiene que ser visible y habilitado"
        assert pass_field.is_displayed() and pass_field.is_enabled(), "Campo Password tiene que ser visible y habilitado"
        mail_field.click()
        mail_field.send_keys(f"{usuario_input}")
        pass_field.click()
        pass_field.send_keys(f"{password_input}")

        login_btn = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        login_btn.click()
        time.sleep(5)


        login_error_msg = self.driver.find_element(By.CLASS_NAME, "alert-danger")
        assert login_error_msg.is_enabled(), "Mensaje error login debe ser visible"
        assert exp_error_login_msg in login_error_msg.text, f"Mensaje de confirmacion debe ser {exp_error_login_msg}"


    #Cierra navegador
    def teardown_method(self):
        self.driver.quit()