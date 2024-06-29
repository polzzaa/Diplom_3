from pages.recover_password_page import RecoverPasswordPage
from pages.main_page import MainPage

import allure

class TestRecoverPassword:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_on_recovery_button(self, driver):
        recover_page = RecoverPasswordPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        recover_page.click_on_recover_password_button()
        recover_page.check_recovery_pass_page_open()

    @allure.title('Тест ввода почты и клика по кнопке "Восстановить"')
    def test_set_email_and_click_on_recovery_button(self, driver, create_user):
        recover_page = RecoverPasswordPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        recover_page.click_on_recover_password_button()
        recover_page.set_email_and_click_on_recover_button(create_user[0]["email"])
        recover_page.check_update_password_page()

    @allure.title('Тест клика по кнопке показать/скрыть пароль')
    def test_click_on_show_password_button(self, driver, create_user):
        recover_page = RecoverPasswordPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        recover_page.click_on_recover_password_button()
        recover_page.set_email_and_click_on_recover_button(create_user[0]["email"])
        recover_page.click_on_show_password_but()
        recover_page.check_show_pass()





