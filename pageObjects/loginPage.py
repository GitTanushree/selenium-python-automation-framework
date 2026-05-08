from selenium.webdriver.common.by import By
from pageObjects.basePage import BasePage


class LoginPage(BasePage):
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def enter_username(self, username):
        field = self.wait_for_visibility(*self.username_field)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait_for_visibility(*self.password_field)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait_for_clickable(*self.login_button).click()

    def is_login_successful(self):
        try:
            self.wait_for_visibility(*self.dashboard_header)
            return True
        except:
            return False

    def get_error_message(self):
        return self.wait_for_visibility(*self.error_message).text