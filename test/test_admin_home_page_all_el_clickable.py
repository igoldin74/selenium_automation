

def test_all_elements_clickable_ver_1(app):  # using taditional loop 
    app.open_admin_login_page()
    app.wd.find_element_by_css_selector("[type='text']").clear()
    app.wd.find_element_by_css_selector("[type='text']").send_keys("admin")
    app.wd.find_element_by_css_selector("[type='password']").send_keys("admin")
    app.wd.find_element_by_name("login").click()
    items = app.wd.find_elements_by_css_selector('#app-')
    count = len(items)
    for el in range(count):
        items = app.wd.find_elements_by_css_selector('#app-')
        items[el].click()
        nested_items = app.wd.find_elements_by_css_selector("[id^=doc-]")
        if len(nested_items) > 0:
            for el in range(len(nested_items)):
                nested_items = app.wd.find_elements_by_css_selector("[id^=doc-]")
                nested_items[el].click()


def test_all_elements_clickable_ver_2(app):  # using enumerate() function
    app.open_admin_login_page()
    app.wd.find_element_by_css_selector("[type='text']").clear()
    app.wd.find_element_by_css_selector("[type='text']").send_keys("admin")
    app.wd.find_element_by_css_selector("[type='password']").send_keys("admin")
    app.wd.find_element_by_name("login").click()
    items = app.wd.find_elements_by_css_selector('#app-')
    for el, items in enumerate(items):
        items = app.wd.find_elements_by_css_selector('#app-')
        items[el].click()
        nested_items = app.wd.find_elements_by_css_selector("[id^=doc-]")
        if len(nested_items) > 0:
            for el, nested_items in enumerate(nested_items):
                nested_items = app.wd.find_elements_by_css_selector("[id^=doc-]")
                nested_items[el].click()
























