import pytest
from selene import Browser, Config
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    browser = Browser(Config(driver=driver))
    yield browser
    browser.quit()  # Закрываем браузер после теста