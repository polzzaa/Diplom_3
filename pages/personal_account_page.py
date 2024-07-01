from pages.base_page import BasePage
from data import Url
from locators.pesonal_account_locators import PersonalAccountLocators

import allure

class PersonalAccountPage(BasePage):

    @allure.step('Проверка появления кнопки "История заказов"')
    def check_order_history_button(self):
        assert self.check_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик на кнопка "История заказов"')
    def click_on_history_order_button(self):
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка открытия раздела "История закзаов"')
    def check_history_order_open(self):
        assert self.get_current_url() == Url.ORDER_HISTORY

    @allure.step('Клик на кнопку "Выход"')
    def click_on_logout_but(self):
        self.click_on_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step('Проверка выхода из аккаунта')
    def check_logout(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.LOGIN_BUTTON)
        assert self.get_current_url() == Url.LOGIN_URL

    @allure.step('Получение номера заказа в Истории заказов')
    def get_number_order(self):
        self.get_text(PersonalAccountLocators.ORDER_NUMBER)




