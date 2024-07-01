from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

import allure

class TestOrderFeed:

    @allure.title('Тест на появление всплывающего окна при клике на заказ')
    def test_click_on_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page.click_on_order()
        order_feed_page.check_popup_order()

    @allure.title('Тест на отображении заказа из "Истории заказов" в "Ленте заказов"')
    def test_order_displayed_in_order_feed_and_order_history(self, driver,
                                                             create_user, login, create_order):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.click_on_order_feed()
        order_page.get_number_order()
        main_page.click_on_personal_acc_button()
        account_page.click_on_history_order_button()
        account_page.get_number_order()

        assert order_page.get_number_order() == account_page.get_number_order()

    @allure.title('Тест на увеличение счетчика заказов За все время при создании нового')
    def test_counter_orders_all_time(self, driver, create_user, login):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.click_on_order_feed()
        number_orders = order_page.get_number_orders_all_time()
        main_page.click_on_constructor_button()
        main_page.create_order()
        main_page.click_on_order_feed()
        new_number_orders = order_page.get_number_orders_all_time()
        assert int(new_number_orders) == int(number_orders) + 1

    @allure.title('Тест на увеличение счетчика заказов За сегодня при создании нового')
    def test_counter_orders_today(self, driver, create_user, login):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.click_on_order_feed()
        number_orders = order_page.get_number_orders_today()
        main_page.click_on_constructor_button()
        main_page.create_order()
        main_page.click_on_order_feed()
        new_number_orders = order_page.get_number_orders_today()
        assert int(new_number_orders) == int(number_orders) + 1

    @allure.title('Тест на появление номера заказа "В работе" после оформления заказа')
    def test_order_in_progress(self, driver, create_user, login, create_order):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.click_on_order_feed()
        order_in_progress = order_page.get_order_number_in_progress()
        assert create_order in order_in_progress



