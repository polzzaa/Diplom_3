from pages.base_page import BasePage
from data import Url
from locators.recover_password_locators import RecoverPassLocators

import allure

class RecoverPasswordPage(BasePage):

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_on_recover_password_button(self):
        self.click_on_element(RecoverPassLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Проверка открытия окна "Восстановление пароля"')
    def check_recovery_pass_page_open(self):
        assert self.get_current_url() == Url.RECOVERY_PASSWORD

    @allure.step('Заполнение поля email и клик на кнопку "Восстановить"')
    def set_email_and_click_on_recover_button(self, email):
        self.send_keys(RecoverPassLocators.EMAIL_FIELD, email)
        self.click_on_element(RecoverPassLocators.RECOVER_BUTTON)

    @allure.step('Проверка появления кнопки "Сохранить"')
    def check_update_password_page(self):
        assert self.check_element(RecoverPassLocators.SAVE_BUTTON)

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_on_show_password_but(self):
        self.click_on_element(RecoverPassLocators.SHOW_PASS_BUTTON)

    @allure.step('Проверка активности поля "Пароль"')
    def check_show_pass(self):
        assert self.check_element(RecoverPassLocators.ACTIVE_PASS_FIELD)


