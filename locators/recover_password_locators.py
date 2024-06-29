from selenium.webdriver.common.by import By

class RecoverPassLocators:
    recover_password_button = [By.XPATH, "//a[@href='/forgot-password']"] #Кнопка "Восстановить пароль"
    email_field = [By.XPATH, "//input[@name='name']"] #Поле email
    recover_button = [By.XPATH, "//button[text()='Восстановить']"] #Кнопка "Восстановить"
    password_field = [By.XPATH, "//input[@type='password']"] #Поле "Пароль"
    show_pass_button = [By.XPATH, "//div[contains(@class, 'icon-action')]"] #Кнопка показать/скрыть пароль
    active_pass_field = [By.XPATH, "//div[contains(@class, 'input_status_active')]"] #Активность поля "Пароль"
    save_button = [By.XPATH, "//button[text()='Сохранить']"] #Кнопка "Сохранить"



