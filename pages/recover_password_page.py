from pages.base_page import BasePage
from data import Url
from locators.recover_password_locators import RecoverPassLocators

import allure

class RecoverPasswordPage(BasePage):

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_on_recover_password_button(self):
        self.click_on_element(RecoverPassLocators.recover_password_button)

    @allure.step('Проверка открытия окна "Восстановление пароля"')
    def check_recovery_pass_page_open(self):
        assert self.get_current_url() == Url.RECOVERY_PASSWORD

    @allure.step('Заполнение поля email и клик на кнопку "Восстановить"')
    def set_email_and_click_on_recover_button(self, email):
        self.send_keys(RecoverPassLocators.email_field, email)
        self.click_on_element(RecoverPassLocators.recover_button)

    @allure.step('Проверка появления кнопки "Сохранить"')
    def check_update_password_page(self):
        assert self.check_element(RecoverPassLocators.save_button)

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_on_show_password_but(self):
        self.wait_for_element_to_be_clickable(RecoverPassLocators.show_pass_button)
        self.click_on_element(RecoverPassLocators.show_pass_button)

    @allure.step('Проверка активности поля "Пароль"')
    def check_show_pass(self):
        assert self.check_element(RecoverPassLocators.active_pass_field)


