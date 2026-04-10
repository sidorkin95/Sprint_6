import allure
import pytest
from selenium import webdriver

@allure.step('Открываем браузер Firefox')
def launch_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

@allure.step('Закрываем браузер')
def close_browser(driver):
    driver.quit()

@pytest.fixture
def driver():
    driver = launch_browser()
    yield driver
    close_browser(driver)