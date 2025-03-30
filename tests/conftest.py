import shutil
import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

    #selenoid

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    print("🟡 Используем удаленный веб-драйвер через Selenoid")  # Проверка

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


    # локально:

# @pytest.fixture(scope='function')
# def setup_browser():
#     options = Options()
#     # Запускаем локальный браузер
#     driver = webdriver.Chrome(options=options)
#     browser = Browser(Config(driver=driver))
#
#     yield browser  # Возвращаем browser в тест
#
#     # Делаем аттачи
#     attach.add_screenshot(browser)   # Аттач скриншота
#     attach.add_html(browser)         # Аттач HTML-кода страницы
#     attach.add_logs(browser)         # Аттач логов браузера
#     attach.add_video(browser)        # Аттач видео (если поддерживается)
#
#         # Закрываем браузер после выполнения теста
#     browser.quit()

