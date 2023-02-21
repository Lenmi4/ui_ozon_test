from selenium.webdriver.common.by import By


class CartPageLocators:
    BUTTON_ADD = (By.ID, "add-to-cart-sauce-labs-bike-light")  # кнопка добавления товара в корзину
    BUTTON_REMOVE = (By.ID, "remove-sauce-labs-bike-light")  # кнопка удаления товара из корзины в карточке товара
    BUTTON_CART = (By.ID, "shopping_cart_container")  # кнопка корзины
    PRODUCT_TITLE_CART = (By.CLASS_NAME, "inventory_item_name")  # название товара в корзине
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name") # название товара на основной странице
    BUTTON_ADD_2 = (By.ID, "add-to-cart-sauce-labs-backpack") # кнопка добавления 2го товара в корзину
    BUTTON_CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge") # количество товаров в корзине
    CART_REMOVED = (By.CLASS_NAME, "removed_cart_item") # элемент после удаления товара из корзины