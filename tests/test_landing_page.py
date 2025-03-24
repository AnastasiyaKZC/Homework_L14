import allure
from selene import browser, have


@allure.epic("Landing Page Tests")
@allure.feature("Header")
@allure.story("Логотип должен отображаться в хедере")
@allure.title("Проверка наличия логотипа на странице")

def test_logo_is_visible(browser):
    with allure.step("Открываем страницу https://it.arda.digital"):
        browser.open("https://it.arda.digital")
    with allure.step("Проверяем, что в хедере есть изображение с логотипом"):
        browser.element("header img").should(have.attribute("src"))

