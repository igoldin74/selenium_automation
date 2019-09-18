

def test_all_elements_clickable(app):
    app.open_admin_login_page()
    app.wd.find_element_by_css_selector("[type='text']").clear()
    app.wd.find_element_by_css_selector("[type='text']").send_keys("admin")
    app.wd.find_element_by_css_selector("[type='password']").send_keys("admin")
    app.wd.find_element_by_name("login").click()
    app.wd.find_elements_by_css_selector('#app-')[0].click()
    app.wd.find_element_by_css_selector('#doc-template').click()
    app.wd.find_element_by_css_selector('#doc-logotype').click()
    app.wd.find_elements_by_css_selector('#app-')[1].click()
    app.wd.find_element_by_css_selector('#doc-catalog').click()
    app.wd.find_element_by_css_selector('#doc-product_groups').click()
    app.wd.find_element_by_css_selector('#doc-option_groups').click()
    app.wd.find_element_by_css_selector('#doc-manufacturers').click()
    app.wd.find_element_by_css_selector('#doc-suppliers').click()
    app.wd.find_element_by_css_selector('#doc-delivery_statuses').click()
    app.wd.find_element_by_css_selector('#doc-sold_out_statuses').click()
    app.wd.find_element_by_css_selector('#doc-quantity_units').click()
    app.wd.find_element_by_css_selector('#doc-csv').click()
    app.wd.find_elements_by_css_selector('#app-')[2].click()  # countries
    app.wd.find_elements_by_css_selector('#app-')[3].click()  # currencies
    app.wd.find_elements_by_css_selector('#app-')[4].click()  # customers
    app.wd.find_element_by_css_selector('#doc-customers').click()
    app.wd.find_element_by_css_selector('#doc-csv').click()
    app.wd.find_element_by_css_selector('#doc-newsletter').click()
    app.wd.find_elements_by_css_selector('#app-')[5].click()  # geozones
    app.wd.find_elements_by_css_selector('#app-')[6].click()  # lang
    app.wd.find_element_by_css_selector('#doc-languages').click()
    app.wd.find_element_by_css_selector('#doc-storage_encoding').click()
    app.wd.find_elements_by_css_selector('#app-')[7].click()  # modules
    app.wd.find_element_by_css_selector('#doc-jobs').click()
    app.wd.find_element_by_css_selector('#doc-customer').click()
    app.wd.find_element_by_css_selector('#doc-shipping').click()
    app.wd.find_element_by_css_selector('#doc-payment').click()
    app.wd.find_element_by_css_selector('#doc-order_total').click()
    app.wd.find_element_by_css_selector('#doc-order_success').click()
    app.wd.find_element_by_css_selector('#doc-order_action').click()
    app.wd.find_elements_by_css_selector('#app-')[8].click()  # orders
    app.wd.find_element_by_css_selector('#doc-orders').click()
    app.wd.find_element_by_css_selector('#doc-order_statuses').click()
    app.wd.find_elements_by_css_selector('#app-')[9].click()  # pages
    app.wd.find_elements_by_css_selector('#app-')[10].click()  # reports
    app.wd.find_elements_by_css_selector('#app-')[11].click()  # settings
    app.wd.find_element_by_css_selector('#doc-store_info').click()
    app.wd.find_element_by_css_selector('#doc-defaults').click()
    app.wd.find_element_by_css_selector('#doc-general').click()
    app.wd.find_element_by_css_selector('#doc-listings').click()
    app.wd.find_element_by_css_selector('#doc-images').click()
    app.wd.find_element_by_css_selector('#doc-checkout').click()
    app.wd.find_element_by_css_selector('#doc-advanced').click()
    app.wd.find_element_by_css_selector('#doc-security').click()
    app.wd.find_elements_by_css_selector('#app-')[12].click()  # slides
    app.wd.find_elements_by_css_selector('#app-')[13].click()  # tax
    app.wd.find_element_by_css_selector('#doc-tax_classes').click()
    app.wd.find_element_by_css_selector('#doc-tax_rates').click()
    app.wd.find_elements_by_css_selector('#app-')[14].click()  # translations
    app.wd.find_element_by_css_selector('#doc-search').click()
    app.wd.find_element_by_css_selector('#doc-scan').click()
    app.wd.find_element_by_css_selector('#doc-csv').click()
    app.wd.find_elements_by_css_selector('#app-')[15].click()  # users
    app.wd.find_elements_by_css_selector('#app-')[16].click()  # vqmods
    app.wd.find_element_by_css_selector('#doc-vqmods').click()


























