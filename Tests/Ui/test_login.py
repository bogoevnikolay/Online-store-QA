from pages.login_page import LoginPage
from utils.config import EMAIL, PASSWORD

def test_login_valid_user(browser):
    page = LoginPage(browser)
    page.open()
    page.login(EMAIL, PASSWORD)
    assert page.is_logged_in(), "Пользователь смог войти!"