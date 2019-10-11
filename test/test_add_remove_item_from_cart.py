

def test_cart_add_remove_item(app):
    app.open_user_login_page()
    app.user_login(email='user@mail.com', password='password')
    if app.cart_item_count() > 0:
        app.clear_cart()
    app.add_item_to_cart(qty=3, size_idx=1)
    app.clear_cart()



