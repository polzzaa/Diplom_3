from pages.base_page import BasePage
from data import Url
from locators.main_page_locators import MainPageLocators

import allure

class MainPage(BasePage):

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_on_personal_acc_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.personal_account_button)
        self.click_on_element(MainPageLocators.personal_account_button)

    @allure.step('Клик на кнопку "Войти в аккаунт"')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.login_button)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.constructor_button)

    @allure.step('Проверка появления раздела "Конструктор"')
    def check_constructor_appear(self):
        self.wait_for_visibility_of_element(MainPageLocators.assemble_burger_text)
        assert self.check_element(MainPageLocators.assemble_burger_text)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_on_order_feed(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.order_feed_button)
        self.click_on_element(MainPageLocators.order_feed_button)

    @allure.step('Проверка открытия раздела "Лента заказов"')
    def check_order_feed_open(self):
        assert self.get_current_url() == Url.ORDER_FEED

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.bun)

    @allure.step('Проверка всплывающего окна "Детали ингредиента"')
    def check_click_on_ingredient(self):
        assert self.check_element(MainPageLocators.ingredient_details_popup)

    @allure.step('Закрытие всплывающего окна "Детали ингредиента" по крестику')
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.close_popup_but)

    @allure.step('Проверка закрытия всплывающего окна "Детали ингредиента"')
    def check_ingredient_modal_close(self):
        assert self.check_element(MainPageLocators.popup_close)

    @allure.step('Перетаскивание булки в корзину')
    def bun_drag_drop(self):
        self.drag_drop(MainPageLocators.bun, MainPageLocators.burger_constructor_basket)

    @allure.step('Проверка счетчика ингредиента после добавления в корзину')
    def check_ingredient_counter(self):
        assert self.check_element(MainPageLocators.ingredient_counter)

    @allure.step('Проверка наличия кнопки "Оформить заказ"')
    def check_place_order_login_user(self):
        assert self.check_element(MainPageLocators.place_order_button)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_place_order_but(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.place_order_button)
        self.click_on_element(MainPageLocators.place_order_button)

    @allure.step('Закрытие всплывающего окна после оформления заказа')
    def close_popup_new_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.close_popup_new_order)
        self.click_on_element(MainPageLocators.close_popup_new_order)

    @allure.step('Создание заказа')
    def create_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.bun)
        self.bun_drag_drop()
        self.click_on_place_order_but()
        self.check_invisibility(MainPageLocators.default_number_order)
        number = self.get_text(MainPageLocators.order_number_popup)
        self.close_popup_new_order()
        return number








