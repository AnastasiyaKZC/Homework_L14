import allure
from selene import browser, be


class AuthPage:
    def open(self):
        """Открываем страницу авторизации"""
        with allure.step("Открываем страницу https://it.arda.digital"):
            browser.open("https://arda.ws-dev.ru/")
        return self

    def open_auth_form(self):
        """Нажимаем кнопку для открытия формы авторизации"""
        with allure.step("Открываем форму авторизации"):
            browser.element('button.px-4.py-2.mr-5.font-bold').click()
        return self

    def enter_email(self, email):
        """Вводим логин"""
        with allure.step(f"Вводим логин: {email}"):
            browser.element('#email').set_value(email)
        return self

    def enter_password(self, password):
        """Вводим пароль"""
        with allure.step("Вводим пароль"):
            browser.element('[placeholder="Введите пароль"]').set_value(password)
        return self

    def submit(self):
        """Отправляем форму авторизации"""
        with allure.step("Отправляем форму"):
            browser.element('[type="submit"]').click()
        return self

