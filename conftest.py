import pytest
from selenium import webdriver

from pages.application import Application


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(driver=webdriver.Chrome(), url=base_url)
    #fixture.driver.set_window_size(1920, 1080)
    yield fixture
    fixture.quit()


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
