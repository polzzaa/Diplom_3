import pytest
from selenium import webdriver
import faker
import requests
from data import Url, Api

from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


from locators.pesonal_account_locators import PersonalAccountLocators


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    driver.get(Url.MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
def create_user():

    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Url.MAIN_URL + Api.CREATE_USER, data=payload)

    yield payload, response
    requests.delete(Url.MAIN_URL + Api.DELETE_USER, headers={'Authorization': response.json()['accessToken']})


@pytest.fixture
def login(driver, create_user):
    base = BasePage(driver)
    base.click_on_element(MainPageLocators.personal_account_button)
    base.send_keys(PersonalAccountLocators.email_input, create_user[0]["email"])
    base.send_keys(PersonalAccountLocators.password_input, create_user[0]["password"])
    base.click_on_element(PersonalAccountLocators.login_button)

@pytest.fixture
def create_order(driver):
    main_page =MainPage(driver)
    main_page.bun_drag_drop()
    main_page.click_on_place_order_but()
    main_page.close_popup_new_order()





