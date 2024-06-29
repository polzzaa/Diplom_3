import allure

from pages.main_page import MainPage

class TestMainPage:

    @allure.title('Тест перехода на по клику на "Конструктор"')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        main_page.click_on_constructor_button()
        main_page.check_constructor_appear()

    @allure.title('Тест перехода по клику на "Лента заказов"')
    def test_order_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.check_order_feed_open()

    @allure.title('Тест на появление всплывающего окна по клику на ингредиент')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.check_click_on_ingredient()

    @allure.title('Тест закрытия всплывающего окна по клику на крестик')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_ingredient_modal()
        main_page.check_ingredient_modal_close()

    @allure.title('Тест увеличения счетчика при добавлении ингредиента в заказ')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.bun_drag_drop()
        main_page.check_ingredient_counter()

    @allure.title('Тест на возможность оформить заказ залогиненному пользователю')
    def test_place_order_login_user(self, driver, create_user, login):
        main_page = MainPage(driver)
        main_page.check_place_order_login_user()



