import logging
import time

from selenium.webdriver.remote.webelement import WebElement
from locators.login import LoginPageLocators
from models.auth import AuthData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):

    def is_auth(self):
        if self.find_element(LoginPageLocators.BUTTON_ACCOUNT):
            return True
        return False

    def email_input(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.EMAIL)

    def password_input(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.PASSWORD)

    def button_click(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.BUTTON)

    def exit(self):
        button_account = self.app.driver.find_element(*LoginPageLocators.BUTTON_ACCOUNT)
        self.click_element(button_account)
        button_exit = self.app.driver.find_element(*LoginPageLocators.EXIT)
        time.sleep(3)
        self.click_element(button_exit)

    def auth_error(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.ERROR)

    def auth(self, data: AuthData):
        logger.info(f'User email is "{data.login}"')
        logger.info(f'User password is "{data.password}"')
        # if self.is_auth():
        #     self.click_element(self.account())
        #     self.click_element(self.exit())
        # self.click_element(self.modal_window_close())
        # self.click_element(self.sign_in())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.button_click())

    def full_page(self):
        return self.app.driver.find_element(*LoginPageLocators.FULL_PAGE)
