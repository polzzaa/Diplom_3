from pages.base_page import BasePage
from data import Url
from locators.main_page_locators import MainPageLocators

import allure

class MainPage(BasePage):

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_on_personal_acc_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Войти в аккаунт"')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка появления раздела "Конструктор"')
    def check_constructor_appear(self):
        assert self.check_element(MainPageLocators.ASSAMBLE_BURGER_TEXT)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_on_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверка открытия раздела "Лента заказов"')
    def check_order_feed_open(self):
        assert self.get_current_url() == Url.ORDER_FEED

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.BUN)

    @allure.step('Проверка всплывающего окна "Детали ингредиента"')
    def check_click_on_ingredient(self):
        assert self.check_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Закрытие всплывающего окна "Детали ингредиента" по крестику')
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUT)

    @allure.step('Проверка закрытия всплывающего окна "Детали ингредиента"')
    def check_ingredient_modal_close(self):
        assert self.check_element(MainPageLocators.POPUP_CLOSE)

    @allure.step('Перетаскивание булки в корзину')
    def bun_drag_drop(self):
        self.drag_drop(MainPageLocators.BUN, MainPageLocators.BURGER_CONSTRUCTOR_BUTTON)

    @allure.step('Проверка счетчика ингредиента после добавления в корзину')
    def check_ingredient_counter(self):
        assert self.check_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Проверка наличия кнопки "Оформить заказ"')
    def check_place_order_login_user(self):
        assert self.check_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_place_order_but(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Закрытие всплывающего окна после оформления заказа')
    def close_popup_new_order(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_NEW_ORDER)

    @allure.step('Создание заказа')
    def create_order(self):
        self.bun_drag_drop()
        self.click_on_place_order_but()
        self.check_invisibility(MainPageLocators.DEFAULT_NUMBER_ORDER)
        number = self.get_text(MainPageLocators.ORDER_NUMBER_POPUP)
        self.close_popup_new_order()
        return number








