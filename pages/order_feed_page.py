from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

import allure

class OrderFeedPage(BasePage):

    @allure.step('Клик на заказ')
    def click_on_order(self):
        self.wait_for_element_to_be_clickable(OrderFeedLocators.orders)
        self.click_on_element(OrderFeedLocators.orders)

    @allure.step('Проверка всплывающего окна "Детали заказа"')
    def check_popup_order(self):
        assert self.check_element(OrderFeedLocators.popup_orders)

    @allure.step('Получение номера заказа в Ленте заказов')
    def get_number_order(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.order_number_in_order_feed)
        self.get_text(OrderFeedLocators.order_number_in_order_feed)

    @allure.step('Получение количества заказов за все время')
    def get_number_orders_all_time(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.orders_for_all_time)
        return self.get_text(OrderFeedLocators.orders_for_all_time)

    @allure.step('Получение количества заказов за сегодня')
    def get_number_orders_today(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.orders_for_today)
        return self.get_text(OrderFeedLocators.orders_for_today)

    @allure.step('Получение номера заказа в работе')
    def get_order_number_in_progress(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.order_in_progress)
        return self.get_text(OrderFeedLocators.order_in_progress)