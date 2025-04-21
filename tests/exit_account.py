from locators import BurgerLocators
from data import BurgerTestData
import settings
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestExitAccount:
    def test_exit_account(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        driver.find_element(*BurgerLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'account/profile'))
        driver.find_element(*BurgerLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'login'))

        login_title = driver.find_element(*BurgerLocators.TITLE_ENTER)
        assert login_title.is_displayed() and login_title.text == 'Вход'
