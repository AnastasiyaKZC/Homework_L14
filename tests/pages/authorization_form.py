from selene import browser, have, be
from selene.support.shared import browser as setup_browser

class LoginForm:
    def __init__(self):
        setup_browser.open("https://it.arda.digital")  # Открытие лендинга
        browser.element(".login-button").click()  # Клик по элементу для перехода на страницу авторизации
        self.form = browser.element("form")  # Форма авторизации
        self.email = self.form.element("input[name='email']")  # Поле для ввода email
        self.password = self.form.element("input[name='password']")  # Поле для ввода пароля
        self.submit = self.form.element("button[type='submit']")  # Кнопка отправки формы

    def login(self, email, password):
        self.email.set_value(email)  # Ввод email
        self.password.set_value(password)  # Ввод пароля
        self.submit.click()  # Нажатие на кнопку входа
        return self

    def should_have_error(self, message):
        browser.element("#app > div > div.fixed.backdrop-blur-sm.left-0.top-0.z-50.bg-background.w-full.h-screen.overflow-auto.flex > div > div > div > form > div:nth-child(2) > div > span").should(be.visible).should(have.text(message))  # Проверка наличия сообщения об ошибке
        return self
