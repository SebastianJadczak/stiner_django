import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    """Klasa bazowa inicjalizująca driver'a i zamykająca przeglądarkę po wykonaniu testu"""

    adres = 'https://stiner-dev.herokuapp.com/'

    @pytest.fixture()
    def setup(self):
        """Inicjalizacja przeglądarki, opóźnienie maksymalizacji okna oraz zamknięcie okna przeglądarki po zakończeniu testu"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.quit()
