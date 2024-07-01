from selenium.webdriver.common.by import By

class RecoverPassLocators:
    RECOVER_PASSWORD_BUTTON = [By.XPATH, "//a[@href='/forgot-password']"] #Кнопка "Восстановить пароль"
    EMAIL_FIELD = [By.XPATH, "//input[@name='name']"] #Поле email
    RECOVER_BUTTON = [By.XPATH, "//button[text()='Восстановить']"] #Кнопка "Восстановить"
    PASSWORD_FIELD = [By.XPATH, "//input[@type='password']"] #Поле "Пароль"
    SHOW_PASS_BUTTON = [By.XPATH, "//div[contains(@class, 'icon-action')]"] #Кнопка показать/скрыть пароль
    ACTIVE_PASS_FIELD = [By.XPATH, "//div[contains(@class, 'input_status_active')]"] #Активность поля "Пароль"
    SAVE_BUTTON = [By.XPATH, "//button[text()='Сохранить']"] #Кнопка "Сохранить"



