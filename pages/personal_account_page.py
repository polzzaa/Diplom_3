from pages.base_page import BasePage
from data import Url
from locators.pesonal_account_locators import PersonalAccountLocators

import allure

class PersonalAccountPage(BasePage):

    @allure.step('Проверка появления кнопки "История заказов"')
    def check_order_history_button(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.order_history_button)
        assert self.check_element(PersonalAccountLocators.order_history_button)

    @allure.step('Клик на кнопка "История заказов"')
    def click_on_history_order_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountLocators.order_history_button)
        self.click_on_element(PersonalAccountLocators.order_history_button)

    @allure.step('Проверка открытия раздела "История закзаов"')
    def check_history_order_open(self):
        assert self.get_current_url() == Url.ORDER_HISTORY

    @allure.step('Клик на кнопку "Выход"')
    def click_on_logout_but(self):
        self.wait_for_element_to_be_clickable(PersonalAccountLocators.logout_button)
        self.click_on_element(PersonalAccountLocators.logout_button)

    @allure.step('Проверка выхода из аккаунта')
    def check_logout(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.login_button)
        assert self.get_current_url() == Url.LOGIN_URL

    @allure.step('Получение номера заказа в Истории заказов')
    def get_number_order(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.order_number)
        self.get_text(PersonalAccountLocators.order_number)




