

def test_litecart_login(app):
    app.open_home_page()
    app.wd.find_element_by_name("email").send_keys("user@mail.com")
    app.wd.find_element_by_name("password").send_keys("password")
    app.wd.find_element_by_name("login").click()
    assert app.wd.find_element_by_css_selector(".success")