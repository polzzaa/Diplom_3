from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    login_button = [By.XPATH, "//button[text()='Войти']"]  #Кнопка Войти
    email_input = [By.NAME, "name"]  #Поле ввода email
    password_input = [By.NAME, "Пароль"]  #Поле ввода пароля
    order_history_button = [By.XPATH, "//a[text()='История заказов']"] #Кнопка "История заказов"
    logout_button = [By.XPATH, "//button[text()='Выход']"] #Кнопка "Выход"
    order_number = [By.XPATH, "//p[@class='text text_type_digits-default']"] #Номер заказа в истории заказов
