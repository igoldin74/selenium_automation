from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_stickers_present(app):
    app.open_user_login_page()
    app.wd.find_element_by_name("email").send_keys("user@mail.com")
    app.wd.find_element_by_name("password").send_keys("password")
    app.wd.find_element_by_name("login").click()
    elements = app.wd.find_elements_by_css_selector('[class^=product]')
    for el in elements:
        assert EC.presence_of_element_located((By.CSS_SELECTOR, "[class^=sticker]"))
