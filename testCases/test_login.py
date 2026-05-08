import pytest
from pageObjects.loginPage import LoginPage
from utilities.readConfig import ReadConfig


class TestLogin:

    def test_valid_login(self, driver):
        """Verify login with valid credentials navigates to Dashboard"""
        login = LoginPage(driver)
        login.enter_username(ReadConfig.get_username())
        login.enter_password(ReadConfig.get_password())
        login.click_login()
        assert login.is_login_successful(), "Login failed — Dashboard not visible"

    def test_invalid_login(self, driver):
        """Verify login with invalid credentials shows error"""
        login = LoginPage(driver)
        login.enter_username("invalid_user")
        login.enter_password("wrong_pass")
        login.click_login()
        error = login.get_error_message()
        assert "Invalid credentials" in error, f"Unexpected error message: {error}"