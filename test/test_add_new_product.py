import os.path
from selenium.webdriver.support.ui import Select


def test_add_new_product_to_cat(app):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resource/logo.png')
    app.open_admin_login_page()
    app.admin_login(user='admin', password='admin')
    app.wd.find_elements_by_css_selector('#app-')[1].click()
    item_list = app.wd.find_elements_by_css_selector('.row')
    app.wd.find_elements_by_css_selector('.button')[1].click()
    tabs = app.wd.find_elements_by_css_selector('#content li a')
    app.wd.find_element_by_css_selector('label:nth-child(3) input[value="1"]').click()
    app.wd.find_element_by_name('name[en]').send_keys("test_product")
    app.wd.find_element_by_name('code').send_keys("test_code")
    app.wd.find_element_by_css_selector('[data-name = "Rubber Ducks"]').click()
    app.wd.find_element_by_name('product_groups[]').click()
    app.wd.find_element_by_name('quantity').clear()
    app.wd.find_element_by_name('quantity').send_keys('100')
    app.wd.find_element_by_css_selector('[type="file"]').send_keys(file_path)
    app.wd.find_element_by_name('date_valid_from').send_keys('2019-09-20')
    app.wd.find_element_by_name('date_valid_to').send_keys('2020-09-20')
    tabs[1].click()
    Select(app.wd.find_element_by_name('manufacturer_id')).select_by_value('1')
    app.wd.find_element_by_name('keywords').send_keys('test tester qa')
    app.wd.find_element_by_name('short_description[en]').send_keys('test')
    app.wd.find_element_by_css_selector('.trumbowyg-editor').send_keys('test')
    app.wd.find_element_by_name('head_title[en]').send_keys('test')
    app.wd.find_element_by_name('meta_description[en]').send_keys('test')
    tabs[3].click()
    app.wd.find_element_by_name('purchase_price').send_keys('5')
    Select(app.wd.find_element_by_name('purchase_price_currency_code')).select_by_value('USD')
    app.wd.find_element_by_name('prices[USD]').send_keys('100')
    app.wd.find_element_by_name('prices[EUR]').send_keys('90')
    app.wd.find_element_by_name('save').click()
    new_item_list = app.wd.find_elements_by_css_selector('.row')
    assert len(new_item_list) == len(item_list) + 1
