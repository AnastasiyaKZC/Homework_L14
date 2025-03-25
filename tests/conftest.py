import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

    #selenoid

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver=driver))
    yield browser  # Возвращаем browser в тест
    attach.add_screenshot(browser)
    attach.add_html(browser)
    try:
        attach.add_logs(browser)
    except Exception:
        print("⚠️ Не удалось получить логи браузера!")
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
#     # Закрываем браузер после выполнения теста, но сначала делаем аттачи
#     attach.add_screenshot(browser)  # Аттач скриншота
#     attach.add_html(browser)         # Аттач HTML-кода страницы
#     attach.add_logs(browser)         # Аттач логов браузера
#     attach.add_video(browser)        # Аттач видео (если поддерживается)
#
#         # Закрываем браузер после выполнения теста
#     browser.quit()
