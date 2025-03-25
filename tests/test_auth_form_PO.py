import allure
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from selene import browser, be

@allure.epic("Authorization Form Tests")
@allure.feature("Authorization Form")
@allure.story("Проверка отправки пустой формы")
@allure.title("Проверка ошибки при отправке пустой формы (page_object)")
def test_empty_auth_form(setup_browser):
    auth_page = AuthPage()
    (
        auth_page.open()
        .open_auth_form()
        .submit()
    )
    # Проверяем, что отображаются ошибки ввода
    browser.element("span.text-red").should(be.visible)

@allure.epic("Authorization Form Tests")
@allure.feature("Authorization Form")
@allure.story("Пользователь должен успешно авторизоваться")
@allure.title("Проверка успешной авторизации (page_object)")
def test_successful_authorization_2(setup_browser):
    auth_page = AuthPage()
    main_page = MainPage()
    (
        auth_page.open()
        .open_auth_form()
        .enter_email("member@arda.digital")
        .enter_password("111111")
        .submit()
    )

    main_page.should_have_user_menu()