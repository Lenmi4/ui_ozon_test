
from locators.cart import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):

    def button_add(self):
        add = self.app.driver.find_element(*CartPageLocators.BUTTON_ADD)
        self.click_element(add)

    def button_remove(self):
        remove = self.app.driver.find_element(*CartPageLocators.BUTTON_REMOVE)
        self.click_element(remove)

    def cart_shopping(self):
        cart = self.app.driver.find_element(*CartPageLocators.BUTTON_CART)
        self.click_element(cart)

    def title_cart(self):
        product_title_cart = self.app.driver.find_element(*CartPageLocators.PRODUCT_TITLE_CART)
        return product_title_cart

    def product_title(self):
        click_product = self.app.driver.find_element(*CartPageLocators.PRODUCT_TITLE)
        return click_product

    def button_add_2(self):
        add_2 = self.app.driver.find_element(*CartPageLocators.BUTTON_ADD_2)
        self.click_element(add_2)

    def count_cart(self):
        count = self.app.driver.find_element(*CartPageLocators.BUTTON_CART_NUMBER)
        return count

    def cart_removed(self):
        self.app.driver.find_element(*CartPageLocators.CART_REMOVED)


