import time

from selenium.webdriver.remote.webelement import WebElement

from locators.login import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def is_auth(self):
        time.sleep(5)
        element = self.find_element(LoginPageLocators.ACCOUNT)
        if element.text == "Лена":
            return True
        return False

    def modal_window_close(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.MODAL_WINDOW_CLOSE)

    def sign_in(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.SIGN_IN)

    def email_input(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.EMAIL)

    def password_input(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.PASSWORD)

    def button_click(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.BUTTON)

    def account(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.ACCOUNT)

    def exit(self) -> WebElement:
        return self.app.driver.find_element(*LoginPageLocators.EXIT)

    def auth_email_error(self) -> str:
        return self.app.driver.find_element(*LoginPageLocators.EMAIL_ERROR).text

    def auth(self, login: str, password: str):
        # if self.is_auth():
        #     self.click_element(self.account())
        #     self.click_element(self.exit())
        self.click_element(self.modal_window_close())
        self.click_element(self.sign_in())
        self.fill_element(self.email_input(), login)
        self.fill_element(self.password_input(), password)
        self.click_element(self.button_click())

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


# def auth(driver, user, password):
#     driver.get('https://www.gloria-jeans.ru/')
#     email = driver.find_element(*LoginPageLocators.EMAIL)
#     passw = driver.find_element(*LoginPageLocators.PASSWORD)
#     email.send_keys(user)
#     passw.send_keys(password)
#     driver.find_element(*LoginPageLocators.BUTTON).click()
#
#
#



