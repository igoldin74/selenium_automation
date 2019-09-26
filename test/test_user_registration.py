from selenium.webdriver.support.ui import Select
from random import uniform


def test_new_user_registration(app):
    prefix = str(uniform(0, 99))
    email = prefix+"test_email@mail.com"
    password = "password"
    app.open_user_login_page()
    app.wd.find_element_by_css_selector('#box-account-login tr td a').click()
    app.wd.find_element_by_name('firstname').send_keys("test_user_firstname")
    app.wd.find_element_by_name('lastname').send_keys("test_user_lastname")
    app.wd.find_element_by_name('address1').send_keys("test_address")
    app.wd.find_element_by_name('postcode').send_keys("60606")
    app.wd.find_element_by_name('city').send_keys("test_city")
    Select(app.wd.find_element_by_name('zone_code')).select_by_visible_text('Illinois')
    app.wd.find_element_by_name('email').send_keys(email)
    app.wd.find_element_by_name('phone').send_keys("5678903434")
    app.wd.find_element_by_name('newsletter').click()
    app.wd.find_element_by_name('password').send_keys(password)
    app.wd.find_element_by_name('confirmed_password').send_keys(password)
    app.wd.find_element_by_name('create_account').click()
    app.wd.find_element_by_css_selector('#box-account li:nth-child(4) a').click()
    app.open_user_login_page()
    app.user_login(email=email, password=password)
    app.wd.find_element_by_css_selector('#box-account li:nth-child(4) a').click()





