from locators import BurgerLocators
from data import BurgerTestData
import settings
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestSuccessfulLogIn:
    def test_successful_log_in_account_button(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))

        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'



    def test_successful_log_in_personal_account(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ACCOUNT).click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

    def test_successful_log_in_registration_form(self, driver):
        driver.get(settings.URL + "login")
        driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

    def test_successful_log_in_reset_password(self, driver):
        driver.get(settings.URL + "login")
        driver.find_element(*BurgerLocators.BUTTON_FORGOT_PASSWORD).click()
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'
