class TestProduct:

    def test_open_product_img(self, app, auth):
        app.goods.img_product()
        assert app.goods.open_product()

    def test_open_product_text(self, app, auth):
        app.goods.text_product()
        assert app.goods.open_product()

    def test_back_to_products(self, app, auth):
        app.goods.img_product()
        app.goods.button_back()
        assert app.goods.main_page()
