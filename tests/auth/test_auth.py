from selenium.webdriver.support.wait import WebDriverWait

from common.constants import LoginConstants
from locators.login import LoginPageLocators
import time

from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData(login="mailavtotests@ya.ru", password='Avto123')
        app.login.auth(data)
        assert app.login.is_auth(), 'We are not auth'


    def test_auth_invalid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData.random()
        app.login.auth(data)
        assert app.login.auth_email_error() == LoginConstants.AUTH_ERROR, 'We are not auth'
