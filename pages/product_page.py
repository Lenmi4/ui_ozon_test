import re

from locators.product import ProductPageLocators
from pages.base_page import BasePage
from common.constants import ProductConstants


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

    def not_correct_name(self):
        name = self.app.driver.find_element(*ProductPageLocators.TEXT_9)
        product_name = name.text
        all_name = re.search(ProductConstants.NOT_CORRECT_SINGS, product_name)
        if all_name is None:
            return all_name
        else:
            return "Product name is not correct"

    def correct_name(self):
        name = self.app.driver.find_element(*ProductPageLocators.TEXT_1)
        product_name = name.text
        all_name = re.search(ProductConstants.NOT_CORRECT_SINGS, product_name)
        if all_name is None:
            return all_name
        else:
            return "Product name is not correct"


