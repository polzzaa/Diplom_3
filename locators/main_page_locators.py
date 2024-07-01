from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"] #Кнопка "Личный кабинет"
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"] #Кнопка "Войти в аккаунт" под корзинов
    ASSAMBLE_BURGER_TEXT = [By.XPATH, "//h1[text()='Соберите бургер']"] #Текст "Соберите бургер" в разделе Конструктор
    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[text()='Конструктор']"] #Кнопка "Конструктор" в хэдере
    ORDER_FEED_BUTTON = [By.XPATH, "//a[@href='/feed']"] #Кнопка "Лента заказов" в хэдере
    INGREDIENT_DETAILS_POPUP = [By.XPATH, "//section[contains(@class, 'modal_opened')]"] #Всплывающее окно "Детали ингредиента"
    BUN = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"] #"Флюоресцентная булка R2-D3"
    CLOSE_POPUP_BUT = [By.XPATH, "//button[contains(@class,'close')]"] #Кнопка закрытия всплывающего окна "Детали ингредиента"
    POPUP_CLOSE = [By.XPATH, "//section[@class='Modal_modal__P3_V5']"] #Закрытое всплывающее окно "Детали ингредиента"
    BURGER_CONSTRUCTOR_BUTTON = [By.XPATH, "//span[@class='constructor-element__text']"] #Счетчик ингредиента
    INGREDIENT_COUNTER = [By.XPATH, "//p[text()=2]"] #Счетчик булки, если она в корзине
    PLACE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"] #Кнопка "Оформить заказ"
    CLOSE_POPUP_NEW_ORDER = [By.XPATH, "//button[contains(@class, 'close')]"] #Кнопка закрытия всплывающего окна после оформления заказа
    ORDER_NUMBER_POPUP = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title_')]"] #Номер заказа во всплывающем окне
    POPUP_ORDER = [By.XPATH, "//div[@class='Modal_modal__P3_V5']"]
    DEFAULT_NUMBER_ORDER = [By.XPATH, '//h2[text()="9999"]'] #Номер заказа по умолчанию







