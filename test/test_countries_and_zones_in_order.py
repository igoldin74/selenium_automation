

def test_countries_and_zones_in_a_z_order(app):
    app.open_admin_login_page()
    app.admin_login(user='admin', password='admin')
    app.wd.find_elements_by_css_selector('#app-')[2].click()
    rows = app.wd.find_elements_by_css_selector('.row')  # finding all rows in the country table
    zone_list = []  # creating empty lists for different properties of rows
    country_list = []
    url_list = []
    for r in rows:  # iterating through rows to append lists with different properties: name, URL, amount of zones
        zone = int(r.find_element_by_css_selector('td:nth-child(6)').get_attribute('innerText'))
        zone_list.append(zone)
        country = r.find_element_by_css_selector('td a').get_attribute('text')
        country_list.append(country)
        url = r.find_element_by_css_selector('td a').get_attribute('href')
        url_list.append(url)
    assert sorted(country_list) == country_list  # testing for country name order against sorted country name list
    merged_url_zone = zip(zone_list, url_list)  # merging two lists together and creating a tuple
    merged_url_zone = tuple(merged_url_zone)
    for key, value in merged_url_zone:  #searching for a key value in tuple that has zone count more thatn 0, then using a value to this key to navigate the link
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


def test_states_in_a_z_order_on_geo_page(app):
    app.open_admin_login_page()
    app.admin_login(user='admin', password='admin')
    app.wd.find_elements_by_css_selector('#app-')[5].click()
    rows = app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')
    for i, rows in enumerate(rows):
        app.wd.find_elements_by_css_selector('#app-')[5].click()
        rows = app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')
        URL = rows[i].get_attribute('href')
        app.wd.get(URL)
        temp = app.wd.find_elements_by_css_selector('#table-zones td:nth-of-type(3) [selected="selected"]')
        states = []
        for i in temp:
            state = i.get_attribute('text')
            states.append(state)
            states = list(filter(None, states))
        assert sorted(states) == states
        print(states)



