import allure
from selene import have, be, browser


@allure.epic("Authorization Form Tests")
@allure.feature("Authorization Form")
@allure.story("Пользователь должен успешно авторизоваться")
@allure.title("Проверка успешной авторизации")
def test_successful_authorization(setup_browser):
    with allure.step("Открываем страницу https://it.arda.digital"):
        setup_browser.open("https://arda.ws-dev.ru/")
    with allure.step("Открываем форму авторизации"):
        setup_browser.element('button.px-4.py-2.mr-5.font-bold').click()
    with allure.step("Вводим логин"):
        setup_browser.element('#email').set_value('member@arda.digital')
    with allure.step("Вводим пароль"):
        setup_browser.element('[placeholder="Введите пароль"]').set_value('111111')
    with allure.step("Отправляем форму"):
        setup_browser.element('[type="submit"]').click()
    # with allure.step("Проверяем, что авторизованы"):


   # with allure.step("Разлогиниваемся?"):