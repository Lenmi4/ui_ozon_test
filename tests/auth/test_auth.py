import pytest
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
        data = AuthData(login="standard_user", password='secret_sauce')
        app.login.auth(data)
        assert app.login.is_auth(), 'We are not auth'

    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_auth_invalid_data(self, app, field):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData.random()
        setattr(data, field, '')
        app.login.auth(data)
        assert app.login.auth_error().text in LoginConstants.AUTH_ERROR, 'We are not auth'

    def test_auth_invalid_password(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData(login="", password='')
        app.login.auth(data)
        assert app.login.auth_error().text in LoginConstants.AUTH_ERROR, 'We are not auth'

    def test_auth_invalid_auth(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData.random()
        app.login.auth(data)
        assert app.login.auth_error().text in LoginConstants.AUTH_ERROR, 'We are not auth'

    def test_auth_logout(self, app): # сделать для проекта тест logout -> exit -> auth
        """
        Steps:
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData(login="standard_user", password='secret_sauce')
        app.login.auth(data)
        assert app.login.is_auth(), 'We are not auth'