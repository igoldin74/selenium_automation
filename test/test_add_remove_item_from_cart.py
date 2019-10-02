from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_cart_add_remove_item(app):
    wait = WebDriverWait(app.wd, 2)
    app.open_user_login_page()
    app.user_login(email='user@mail.com', password='password')
    cart = app.wd.find_element_by_css_selector('#cart .content .quantity')
    item_count = int(cart.get_attribute('textContent'))
    if item_count > 0:
        app.clear_cart()
    for i in range(3):
        app.open_user_login_page()
        items = app.wd.find_elements_by_css_selector('#box-most-popular .image')
        items[0].click()
        drop_list = app.wd.find_elements_by_css_selector('select')
        if len(drop_list) > 0:
            Select(drop_list[0]).select_by_index(1)
        app.wd.find_element_by_name('add_cart_product').click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart .content .quantity'), str(i+1)))
    app.clear_cart()



