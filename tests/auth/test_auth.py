from selenium.webdriver.support.wait import WebDriverWait

from common.constants import LoginConstants
from locators.login import LoginPageLocators
import time


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(login="mailavtotests@ya.ru", password='Avto123')
        assert app.login.is_auth(), 'We are not auth'


    def test_auth_invalid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(login="11111111", password='11111111')
        assert LoginConstants.AUTH_ERROR == app.login.auth_email_error(), 'We are not auth'
