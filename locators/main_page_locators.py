from selenium.webdriver.common.by import By

class MainPageLocators:
    personal_account_button = [By.XPATH, "//a[@href='/account']"] #Кнопка "Личный кабинет"
    login_button = [By.XPATH, "//button[text()='Войти в аккаунт']"] #Кнопка "Войти в аккаунт" под корзинов
    assemble_burger_text = [By.XPATH, "//h1[text()='Соберите бургер']"] #Текст "Соберите бургер" в разделе Конструктор
    constructor_button = [By.XPATH, "//p[text()='Конструктор']"] #Кнопка "Конструктор" в хэдере
    order_feed_button = [By.XPATH, "//a[@href='/feed']"] #Кнопка "Лента заказов" в хэдере
    ingredient_details_popup = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"] #Всплывающее окно "Детали ингредиента"
    bun = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"] #"Флюоресцентная булка R2-D3"
    close_popup_but = [By.XPATH, "//button[contains(@class,'close')]"] #Кнопка закрытия всплывающего окна "Детали ингредиента"
    popup_close = [By.XPATH, "//section[@class='Modal_modal__P3_V5']"] #Закрытое всплывающее окно "Детали ингредиента"
    burger_constructor_basket = [By.XPATH, "//span[@class='constructor-element__text']"] #Счетчик ингредиента
    ingredient_counter = [By.XPATH, "//p[text()=2]"] #Счетчик булки, если она в корзине
    place_order_button = [By.XPATH, "//button[text()='Оформить заказ']"] #Кнопка "Оформить заказ"
    close_popup_new_order = [By.XPATH, "//button[contains(@class, 'close')]"] #Кнопка закрытия всплывающего окна после оформления заказа
    order_number_popup = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title_')]"] #Номер заказа во всплывающем окне
    popup_order = [By.XPATH, "//div[@class='Modal_modal__P3_V5']"]
    default_number_order = [By.XPATH, '//h2[text()="9999"]'] #Номер заказа по умолчанию







