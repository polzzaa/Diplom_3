from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]  #Кнопка Войти
    EMAIL_INPUT = [By.NAME, "name"]  #Поле ввода email
    PASSWORD_INPUT = [By.NAME, "Пароль"]  #Поле ввода пароля
    ORDER_HISTORY_BUTTON = [By.XPATH, "//a[text()='История заказов']"] #Кнопка "История заказов"
    LOGOUT_BUTTON = [By.XPATH, "//button[text()='Выход']"] #Кнопка "Выход"
    ORDER_NUMBER = [By.XPATH, "//p[@class='text text_type_digits-default']"] #Номер заказа в истории заказов
