import pytest
import settings
from locators import BurgerLocators
from data import BurgerTestData
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestJumpFromAccountToConstructor:
    def test_jump_click_constructor(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL))
        driver.find_element(*BurgerLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'account/profile'))
        driver.find_element(*BurgerLocators.BUTTON_CONSTRUCTOR).click()
        title_collect_burger = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed and title_collect_burger.text == 'Соберите бургер'

    def test_jump_from_acc_to_constructor_by_logo(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER_MAIN).click()

        driver.find_element(*BurgerLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*BurgerLocators.LOGO).click()

        title_collect_burger = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed() and title_collect_burger.text == 'Соберите бургер'
