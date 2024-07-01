from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDERS = [By.XPATH, "//a[@class='OrderHistory_link__1iNby']"]  #Лента заказов
    POPUP_ORDERS = [By.XPATH, "//section[contains(@class, 'modal_opened')]"] #Всплывающее окно Детали заказа
    ORDER_NUMBER_IN_ORDER_FEED = [By.XPATH, "//p[@class='text text_type_digits-default']"] #Номер заказа в Ленте заказов
    ORDERS_FOR_ALL_TIME = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] #Количество выполненных заказов за все время
    ORDERS_FOR_TODAY = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] #Количество выполненных заказов за сегодня
    ORDER_IN_PROGRESS = [By.XPATH, "//*[contains(@class,'orderListReady')]//li[contains(@class,'digits-default')]"] #Заказы в работе





