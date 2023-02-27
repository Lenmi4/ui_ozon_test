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

    def test_correct_name(self, app, auth):
        assert app.goods.correct_name() is None, "Product name is not correct"

    def test_not_correct_name(self, app, auth):
        assert app.goods.not_correct_name() is not None, "Product name is correct"
