from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

import  allure
class TestPersonalAccount:

    @allure.title('Тест на переход по клику на "Личный кабинет"')
    def test_click_on_personal_account_but(self, driver, create_user, login):
        main_page = MainPage(driver)
        personal_acc = PersonalAccountPage(driver)

        main_page.click_on_personal_acc_button()
        personal_acc.check_order_history_button()

    @allure.title('Тест перехода в раздел "История заказов"')
    def test_click_on_order_history_but(self, driver, create_user, login):
        main_page = MainPage(driver)
        personal_acc = PersonalAccountPage(driver)

        main_page.click_on_personal_acc_button()
        personal_acc.click_on_history_order_button()
        personal_acc.check_history_order_open()

    @allure.title('Тест на выход из аккаунта')
    def test_logout_account(self, driver, create_user, login):
        main_page = MainPage(driver)
        personal_acc = PersonalAccountPage(driver)

        main_page.click_on_personal_acc_button()
        personal_acc.click_on_logout_but()
        personal_acc.check_logout()






