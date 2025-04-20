import settings
from locators import BurgerLocators
from data import  BurgerTestData
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructorSettings:
    def test_constructor_bread(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        driver.find_element(*BurgerLocators.SAUCE_UNFOCUSED).click()

        driver.find_element(*BurgerLocators.BREAD_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.BREAD_IN_FOCUS)

    def test_constructor_sauce(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))

        driver.find_element(*BurgerLocators.SAUCE_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.SAUCE_IN_FOCUS)

    def test_constructor_topping(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        driver.find_element(*BurgerLocators.SAUCE_UNFOCUSED).click()

        driver.find_element(*BurgerLocators.TOPPING_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.TOPPING_IN_FOCUS)
