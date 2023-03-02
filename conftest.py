import logging
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from models.auth import AuthData
from pages.application import Application

logger = logging.getLogger("moodle")


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption("--base-url")
    logger.info(f'Start moodle {base_url}')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    fixture = Application(webdriver.Chrome(chrome_options=chrome_options), url=base_url)
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    login = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_main_page()
    data = AuthData(login=login, password=password)
    app.login.auth(data)


# @pytest.fixture
# def add_product_in_cart(app):
#     app.cart.button_add()
#     app.cart.cart_shopping()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="standard_user",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="secret_sauce",
        help="enter base_url",
    ),
