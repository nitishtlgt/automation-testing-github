import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_github_login(browser):
    browser.get("https://github.com/login")

    username_field = browser.find_element("id", "login_field")
    password_field = browser.find_element("id", "password")

    username_field.send_keys("Vishal-d-2023")
    password_field.send_keys("Vishal@1@#")

    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    assert browser.find_element("class name", "avatar-user")

if __name__ == "__main__":
    pytest.main([__file__])
