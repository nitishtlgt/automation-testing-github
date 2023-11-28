import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    options.binary_location = "/home/ubuntu/Downloads/chromedriver.exe"    
    options.add_argument("--start-maximized") 
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(options=options, executable_path="/home/ubuntu/Downloads/chromedriver.exe")

    # options = Options()
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # # driver = webdriver.Chrome(options=chrome_options)
    # driver_path = ChromeDriverManager().install()
    # driver = webdriver.Chrome(options=chrome_options)
    # # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
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
