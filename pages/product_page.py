from locators.product import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def img_product(self):
        img = self.app.driver.find_element(*ProductPageLocators.IMG_1)
        self.click_element(img)

    def open_product(self):
        product = self.app.driver.find_element(*ProductPageLocators.PRODUCT_1)
        return product

    def text_product(self):
        text = self.app.driver.find_element(*ProductPageLocators.TEXT_1)
        self.click_element(text)

    def button_back(self):
        back = self.app.driver.find_element(*ProductPageLocators.BUTTON_BACK)
        self.click_element(back)

    def main_page(self):
        main = self.app.driver.find_element(*ProductPageLocators.MAIN_PAGE)
        return main
