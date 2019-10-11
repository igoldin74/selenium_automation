from selenium.webdriver.support.ui import Select


class ItemPage:

    def __init__(self, wd):
        self.wd = wd

    def size_drop_list(self):
        return self.wd.find_elements_by_css_selector('select')

    def select_size(self, index):
        if len(self.size_drop_list()) > 0:
            Select(self.size_drop_list()[0]).select_by_index(index)
        return self

    def click_add_to_cart_button(self):
        self.wd.find_element_by_name('add_cart_product').click()
        return self

    def cart(self):
        return self.wd.find_element_by_css_selector('#cart .content .quantity')
