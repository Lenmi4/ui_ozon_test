import pytest
from selenium import webdriver

from pages.application import Application


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(driver=webdriver.Chrome(), base_url)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        defult="https://www.gloria-jeans.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        defult="mailavtotests@ya.ru",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        defult="Avto123",
        help="enter base_url",
    ),
