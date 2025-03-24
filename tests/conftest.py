# import pytest
# from selene import Browser, Config
# from selenium import webdriver
#
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     browser = Browser(Config(driver=driver))
#     yield browser
#     browser.quit()  # Закрываем браузер после теста


import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
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
    # ✅ Важно: сначала делаем аттачи, потом закрываем браузер!
    attach.add_screenshot(browser)
    attach.add_html(browser)

    try:
        attach.add_logs(browser)
    except Exception:
        print("⚠️ Не удалось получить логи браузера!")

    attach.add_video(browser)

    browser.quit()  # ✅ Теперь закрываем браузер