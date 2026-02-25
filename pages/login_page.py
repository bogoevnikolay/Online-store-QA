from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def open(self):
        self.driver.get("https://automationexercise.com/login")# ссылка на страницу логина

    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.is_visible(LoginLocators.LOGGED_IN_TEXT)