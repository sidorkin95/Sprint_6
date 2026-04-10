import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture
def driver():   
    
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.quit()
    
    
@pytest.fixture
def open_main_page(driver):
    driver.get(Urls.BASE_URL)
    return driver