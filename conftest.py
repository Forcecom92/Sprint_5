from selenium import webdriver
import pytest
import settings



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1296, 756)
    driver.get(settings.URL)

    yield driver

    driver.quit()












