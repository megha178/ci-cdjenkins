import time
import pytest
import allure

from selenium import webdriver
from src.pageObjects.loginPage import LoginPage
from src.utils.ExcelRader import ExcelReader
from selenium.webdriver.common.by import By


class TestVWOLogin:
    @pytest.mark.smoke
    @allure.feature('#TC -1 ,verify scenarios for login functionality with combination of username and password')
    @pytest.mark.parametrize("username, password, result", ExcelReader(
        "/Users/megha/PycharmProject/pywebautomationframework/src/utils/test_data.xlsx").read_sheet("Sheet1"))
    @pytest.mark.usefixtures("setup")
    #   def test_vwologin(self, setup):
    def test_vwo_login(self, username, password, result, setup):
        driver = setup
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(username, password)

        if result == "fail":
            assert "Your email, password, IP address or location did not match" in loginPage.get_errormessage().text
            driver.quit()
        else:
            assert "https://app.vwo.com/#/dashboard" in driver.current_url
