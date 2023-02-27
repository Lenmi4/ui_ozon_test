from selenium.webdriver.common.by import By


class ProductPageLocators:
    IMG_1 = (By.ID, "item_4_img_link")  # фото товара на основной странице
    TEXT_1 = (By.ID, "item_4_title_link") # область названия товара
    PRODUCT_1 = (By.ID, "inventory_item_container") # открытая карточка товара
    BUTTON_BACK = (By.ID, "back-to-products") # кнопка возврата к списку товаров из карточки товара
    MAIN_PAGE = (By.ID, "root") # основная страница со всеми товарами
