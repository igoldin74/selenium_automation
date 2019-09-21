
#  first version I wanted to implement
def test_countries_and_zones_in_a_z_order(app):
    app.open_admin_login_page()
    app.wd.find_element_by_css_selector("[type='text']").clear()
    app.wd.find_element_by_css_selector("[type='text']").send_keys("admin")
    app.wd.find_element_by_css_selector("[type='password']").send_keys("admin")
    app.wd.find_element_by_name("login").click()
    app.wd.find_elements_by_css_selector('#app-')[2].click()
    rows = app.wd.find_elements_by_css_selector('.row')
    countries = app.wd.find_elements_by_css_selector('.row td a') 
    zones = app.wd.find_elements_by_css_selector('.row td:nth-child(6)')
    country_list = []
    for i in countries:
        text = i.get_attribute('text')
        country_list.append(text)
    del country_list[1::2]
    a_z_list = sorted(country_list)
    assert country_list == a_z_list
    for i in zones:
        if int(i.get_attribute("innerText")) > 0:
            pass

#  second version I decided to go with:
def test_countries_and_zones_in_a_z_order_ver1(app):
    app.open_admin_login_page()
    app.admin_login(user="admin", password="admin")
    app.wd.find_elements_by_css_selector('#app-')[2].click()
    rows = app.wd.find_elements_by_css_selector('.row')
    zone_list = []
    country_list = []
    url_list = []
    for r in rows:
        zone = int(r.find_element_by_css_selector('td:nth-child(6)').get_attribute("innerText"))
        zone_list.append(zone)
        country = r.find_element_by_css_selector('td a').get_attribute("text")
        country_list.append(country)
        url = r.find_element_by_css_selector('td a').get_attribute("href")
        url_list.append(url)
    assert sorted(country_list) == country_list
    merged_url_zone = zip(zone_list, url_list)
    merged_url_zone = set(merged_url_zone)
    for key, value in merged_url_zone:
        if key > 0:
            app.wd.get(value)
            temp = app.wd.find_elements_by_css_selector('#table-zones > tbody > tr > td:nth-child(3)')
            states = []
            for e in temp:
                state = e.get_attribute('innerText')
                states.append(state)
                states = list(filter(None, states))
                assert sorted(states) == states
        else:
            pass
