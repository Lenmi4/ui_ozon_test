from common.constants import CartConstants
import time
import allure


@allure.description("добавление товара в корзину с основной страницы")
class TestShoppingCart:
    def test_add_prod_main_page(self, app, auth):
        """
        Steps:
        1. Auth with valid data
        2. Add a product to the shopping cart
        3. The cart shopping displays the number of items
        """
        app.cart.button_add_click()
        app.cart.cart_shopping()
        assert app.cart.title_cart().text == CartConstants.PRODUCT_TITLE, "Product not add in the cart"

    def test_add_products_main_page(self, app, auth):  # добавление 2х товаров в корзину с основной страницы
        """
        Steps:
        1. Auth with valid data
        2. Add a product to the shopping cart
        3. The cart shopping displays the number of items
        """
        app.cart.button_add_click()
        app.cart.button_add_2()
        app.cart.cart_shopping()
        # time.sleep(3)
        assert app.cart.count_cart().text == "2"

    def test_add_prod(self, app, auth):  # добавление товара в корзину из карточки товара
        """
        Steps:
        1. Auth with valid data
        2. Click on product cart
        3. Add a product to the shopping cart
        4. The cart shopping displays the number of items
        """
        app.cart.title_cart()
        app.cart.button_add_click()
        app.cart.cart_shopping()
        assert app.cart.title_cart().text == CartConstants.PRODUCT_TITLE, "Product not add in the cart"

    def test_del_prod_shop(self, app, auth):  # удаление товара из корзины
        """
        Steps:
        1. Auth with valid data
        2. Click on product cart
        3. Add a product to the shopping cart
        4. Delete a product from the shopping cart
        5. The product not in shopping cart
        """
        app.cart.button_add_click()
        app.cart.cart_shopping()
        app.cart.button_remove()
        assert app.cart.cart_removed() is None

    def test_del_prod_main(self, app, auth):  # удаление товара из корзины с основной страницы
        """
        Steps:
        1. Auth with valid data
        2. Add a product to the shopping cart
        3. The cart shopping displays the number of items
        4. Click button 'Remove'
        5. The cart shopping displays the numbers of items
        """
        app.cart.button_add_click()
        app.cart.button_remove()
        assert app.cart.button_add().text == CartConstants.BUTTON_ADD_NAME

    def test_del_prod_card(self, app, auth):  # удаление товара из корзины со страницы карточки товара
        """
        Steps:
        1. Auth with valid data
        2. Click on product card
        3. Add a product to the shopping card
        4. The cart shopping displays the number of items
        6. Click button 'Remove'
        7. The cart shopping displays the numbers of items
        """
        app.cart.title_cart()
        app.cart.button_add_click()
        # time.sleep(3)
        app.cart.button_remove()
        assert app.cart.button_add().text == CartConstants.BUTTON_ADD_NAME
