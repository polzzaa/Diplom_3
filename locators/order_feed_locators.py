from selenium.webdriver.common.by import By

class OrderFeedLocators:
    orders = [By.XPATH, "//a[@class='OrderHistory_link__1iNby']"]  #Лента заказов
    popup_orders = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"] #Всплывающее окно Детали заказа
    order_number_in_order_feed = [By.XPATH, "//p[@class='text text_type_digits-default']"] #Номер заказа в Ленте заказов
    orders_for_all_time = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] #Количество выполненных заказов за все время
    orders_for_today = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] #Количество выполненных заказов за сегодня
    order_in_progress = [By.XPATH, "//*[contains(@class,'orderListReady')]//li[contains(@class,'digits-default')]"] #Заказы в работе





