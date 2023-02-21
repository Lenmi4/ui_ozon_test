import time

from selenium.webdriver.remote.webelement import WebElement
from locators.login import LoginPageLocators
from models.auth import AuthData
from pages.base_page import BasePage


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
        # if self.is_auth():
        #     self.click_element(self.account())
        #     self.click_element(self.exit())
        #self.click_element(self.modal_window_close())
        #self.click_element(self.sign_in())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.button_click())

    def full_page(self):
        return self.app.driver.find_element(*LoginPageLocators.FULL_PAGE)





    # def auth(self, login: str, password: str):
    #     modal_window_close = self.app.driver.find_element(*LoginPageLocators.MODAL_WINDOW_CLOSE)
    #     modal_window_close.click()
    #     sign_in = self.app.driver.find_element(*LoginPageLocators.SIGN_IN)
    #     sign_in.click()
    #     email_input = self.app.driver.find_element(*LoginPageLocators.EMAIL)
    #     email_input.send_keys(login)
    #     password_input = self.app.driver.find_element(*LoginPageLocators.PASSWORD)
    #     password_input.send_keys(password)
    #     button_click = self.app.driver.find_element(*LoginPageLocators.BUTTON)
    #     button_click.click()




