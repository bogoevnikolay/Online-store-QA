from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")