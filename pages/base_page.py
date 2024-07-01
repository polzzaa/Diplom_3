from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.wait_for_element_to_be_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание появления элемента')
    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        self.wait_for_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Заполнение поля')
    def send_keys(self, locator, text):
        self.wait_for_element_to_be_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Проверка наличия элемента')
    def check_element(self, locator):
        self.wait_for_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Получение Url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перетаскивание элемента')
    def drag_drop(self, source_element, target_element):
        self.wait_for_element_to_be_clickable(source_element)
        source_element = self.driver.find_element(*source_element)
        target_element = self.driver.find_element(*target_element)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('Проверка отсутствия элемента')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

