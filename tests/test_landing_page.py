import allure
from selene import have, be, browser


@allure.epic("Landing Page Tests")
@allure.feature("Header")
@allure.story("Логотип должен отображаться в хедере")
@allure.title("Проверка наличия логотипа на странице")
def test_logo_is_visible(setup_browser):
    with allure.step("Открываем страницу https://it.arda.digital"):
        setup_browser.open("https://it.arda.digital")
    with allure.step("Проверяем, что в хедере есть изображение с логотипом"):
        setup_browser.element("header img").should(have.attribute("src"))

@allure.epic("Landing Page Tests")
@allure.feature("Registration Form")
@allure.story("Форма регистрации должна открываться по клику на кнопку")
@allure.title("Проверка открытия формы регистрации")
def test_registration_form_opens(setup_browser):
    with allure.step("Открываем страницу https://it.arda.digital"):
        setup_browser.open("https://it.arda.digital")
    with allure.step("Кликаем на кнопку регистрации"):
        setup_browser.element("span.w-full.relative.inline-block.px-8.py-3.text-sm.font-bold.tracking-widest.text-black.uppercase.border-2.border-current.group-active\\:text-opacity-75").click()
    with allure.step("Проверяем, что форма регистрации отображается"):
        setup_browser.element("form").should(be.visible)


# @allure.epic("Landing Page Tests")
# @allure.feature("Navigation")
# @allure.story("Переход по ссылке arda.digital")
# @allure.title("Проверка корректности перехода по ссылке arda.digital")
# def test_learn_more_link(setup_browser):
#     with allure.step("Открываем страницу https://it.arda.digital"):
#         setup_browser.open("https://it.arda.digital")
#     with allure.step("Кликаем на кнопку 'Подробнее'"):
#         setup_browser.element("a[href='/learn-more']").click()
#     with allure.step("Проверяем, что произошел переход на страницу 'Подробнее'"):
#         setup_browser.should(have.url_containing("/learn-more"))
#
