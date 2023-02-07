from locators.login import LoginPageLocators

class LoginPage:

    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        modal_window_close = self.app.driver.find_element(*LoginPageLocators.MODAL_WINDOW_CLOSE)
        modal_window_close.click()
        sigh_in = self.app.driver.find_element(*LoginPageLocators.SIGN_IN)
        sigh_in.click()
        email_input = self.app.driver.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(login)
        password_input = self.app.driver.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        button_click = self.app.driver.find_element(*LoginPageLocators.BUTTON)
        button_click.click()




