from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.cart = CartPage(self)
        self.goods = ProductPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def make_screenshot(self):
        pass


