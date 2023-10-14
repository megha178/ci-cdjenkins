import pytest
from selenium.webdriver import Chrome  # Import the WebDriver class from the correct location
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime

@pytest.fixture()
def driver():
    driver = Chrome()  # Use Chrome() instead of WebDriver.Chrome()
    driver.maximize_window()
    yield driver

def test_login(driver):
    driver.get("https://www.docsmart.in/")
    button_login = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "loginRegister")))
    button_login.click()

    role = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='v-select__selections']")))
    role.click()

    select_role = WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='v-list-item v-list-item--link theme--light'][2]")))
    select_role.click()

    username = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Enter your mobile number here.']/following-sibling::input")))
    username.send_keys("1111111111")

    password = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following-sibling::div//input[@type='password']"))
    )
    password.send_keys("Docsmart@20")

    login = driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
    login.click()
    time.sleep(5)


