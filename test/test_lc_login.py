from selenium.webdriver.common.keys import Keys

def test_litecart_user_login(app):
    app.open_user_login_page()
    app.wd.find_element_by_name("email").send_keys("user@mail.com")
    app.wd.find_element_by_name("password").send_keys("password")
    app.wd.find_element_by_name("login").click()
    assert app.wd.find_element_by_css_selector(".success")


def test_litecart_admin_login(app):
    app.open_admin_login_page()
    alert = app.wd.switch_to_alert()
    alert.send_keys("admin")
    alert.send_keys(Keys.TAB + "admin")
    alert.accept()
    app.wd.find_element_by_css_selector("[type='text']").clear()
    app.wd.find_element_by_css_selector("[type='text']").send_keys("admin")
    app.wd.find_element_by_css_selector("[type='password']").send_keys("admin")
    app.wd.find_element_by_name("login").click()
