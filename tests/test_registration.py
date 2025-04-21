import pytest
import settings
from locators import BurgerLocators
from data import BurgerTestData
from helpers import GeneratorData
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()

        driver.find_element(*BurgerLocators.INPUT_NAME).send_keys(*BurgerTestData.NAME)
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(GeneratorData.generate_logins())
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(GeneratorData.generate_password())
        driver.find_element(*BurgerLocators.BUTTON_FINAL_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'login'))
        success_registration = driver.find_element(*BurgerLocators.TITLE_ENTER)
        assert success_registration.is_displayed() and success_registration.text == 'Вход'

    def test_wrong_password_registration(self, driver):
        button_account = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        button_account.click()

        button_registration = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION)
        button_registration.click()

        driver.find_element(*BurgerLocators.INPUT_NAME).send_keys(*BurgerTestData.NAME)
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.FAKE_EMAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.WRONG_PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_FINAL_REGISTRATION).click()

        wrong_password_registration = driver.find_element(*BurgerLocators.WRONG_PASSWORD)
        assert wrong_password_registration.is_displayed() and wrong_password_registration.text == 'Некорректный пароль'
