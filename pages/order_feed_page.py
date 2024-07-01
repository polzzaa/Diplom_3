from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

import allure

class OrderFeedPage(BasePage):

    @allure.step('Клик на заказ')
    def click_on_order(self):
        self.click_on_element(OrderFeedLocators.ORDERS)

    @allure.step('Проверка всплывающего окна "Детали заказа"')
    def check_popup_order(self):
        assert self.check_element(OrderFeedLocators.POPUP_ORDERS)

    @allure.step('Получение номера заказа в Ленте заказов')
    def get_number_order(self):
        self.get_text(OrderFeedLocators.ORDER_NUMBER_IN_ORDER_FEED)

    @allure.step('Получение количества заказов за все время')
    def get_number_orders_all_time(self):
        return self.get_text(OrderFeedLocators.ORDERS_FOR_ALL_TIME)

    @allure.step('Получение количества заказов за сегодня')
    def get_number_orders_today(self):
        return self.get_text(OrderFeedLocators.ORDERS_FOR_TODAY)

    @allure.step('Получение номера заказа в работе')
    def get_order_number_in_progress(self):
        return self.get_text(OrderFeedLocators.ORDER_IN_PROGRESS)