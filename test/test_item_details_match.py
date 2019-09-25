from selenium.webdriver.support.color import Color


def test_item_details_match_on_home_and_item_page(app):
    app.open_user_login_page()
    app.user_login(email="user@mail.com", password="password")
    item = app.wd.find_element_by_css_selector('#box-campaigns [class = "link"]')
    title = item.get_attribute("title")
    reg_price = item.find_element_by_css_selector('#box-campaigns .price-wrapper [class = "regular-price"]')
    sale_price = item.find_element_by_css_selector('#box-campaigns .price-wrapper [class = "campaign-price"]')
    reg_price_value = reg_price.get_attribute("textContent")
    reg_price_font_color = [Color.from_string(reg_price.value_of_css_property("color")).red,
                            Color.from_string(reg_price.value_of_css_property("color")).green,
                            Color.from_string(reg_price.value_of_css_property("color")).blue]
    reg_price_font_style = reg_price.value_of_css_property("text-decoration-line")
    reg_price_font_size = reg_price.value_of_css_property("font-size")
    sale_price_value = sale_price.get_attribute("textContent")
    sale_price_font_color = [Color.from_string(sale_price.value_of_css_property("color")).red,
                             Color.from_string(sale_price.value_of_css_property("color")).green,
                             Color.from_string(sale_price.value_of_css_property("color")).blue]
    sale_price_font_weight = int(sale_price.value_of_css_property("font-weight"))
    sale_price_font_size = sale_price.value_of_css_property("font-size")
    # open item page:
    item.click()
    item2 = app.wd.find_element_by_css_selector('#box-product')
    title2 = item2.find_element_by_css_selector('.title').get_attribute("textContent")
    reg_price2 = item2.find_element_by_css_selector('#box-product .price-wrapper [class = "regular-price"]')
    sale_price2 = item2.find_element_by_css_selector('#box-product .price-wrapper [class = "campaign-price"]')
    reg_price_value2 = reg_price2.get_attribute("textContent")
    reg_price_font_color2 = [Color.from_string(reg_price2.value_of_css_property("color")).red,
                             Color.from_string(reg_price2.value_of_css_property("color")).green,
                             Color.from_string(reg_price2.value_of_css_property("color")).blue]
    reg_price_font_style2 = reg_price2.value_of_css_property("text-decoration-line")
    reg_price_font_size2 = reg_price2.value_of_css_property("font-size")
    sale_price_value2 = sale_price2.get_attribute("textContent")
    sale_price_font_color2 = [Color.from_string(sale_price2.value_of_css_property("color")).red,
                              Color.from_string(sale_price2.value_of_css_property("color")).green,
                              Color.from_string(sale_price2.value_of_css_property("color")).blue]
    sale_price_font_weight2 = int(sale_price2.value_of_css_property("font-weight"))
    sale_price_font_size2 = sale_price2.value_of_css_property("font-size")
    # assertions
    assert title == title2
    assert reg_price_value == reg_price_value2
    assert sale_price_value == sale_price_value2
    assert sale_price_font_size > reg_price_font_size
    assert sale_price_font_size2 > reg_price_font_size2
    assert 0 in sale_price_font_color[1:]
    assert 0 in sale_price_font_color2[1:]
    assert reg_price_font_style == "line-through"
    assert reg_price_font_style2 == "line-through"
    assert reg_price_font_color[0] == reg_price_font_color[1] == reg_price_font_color[2]
    assert reg_price_font_color2[0] == reg_price_font_color2[1] == reg_price_font_color2[2]
    assert sale_price_font_weight > 0
    assert sale_price_font_weight2 > 0
