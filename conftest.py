import pytest
from selenium import webdriver

from pages.application import Application


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(driver=webdriver.Chrome(), url=base_url)
    fixture.driver.set_window_size(1920, 1080)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.gloria-jeans.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="mailavtotests@ya.ru",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Avto123",
        help="enter base_url",
    ),
