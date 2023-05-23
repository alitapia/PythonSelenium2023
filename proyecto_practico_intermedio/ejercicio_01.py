
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)


    def test_open_page(self):
        # Validar se abra la pagina correcta
        get_url = self.driver.current_url
        assert get_url == URL

    def teardown_method(self):
        self.driver.quit()