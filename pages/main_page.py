import allure
from selene import browser, be


class MainPage:
    def should_have_user_menu(self):
        """Проверяем, что меню пользователя появилось после авторизации"""
        with allure.step("Проверяем наличие меню авторизованного пользователя"):
            browser.element('button.w-auto.flex.justify-center.align-middle').should(be.visible)