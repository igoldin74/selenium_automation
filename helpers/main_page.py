

class MainPage:

    def __init__(self, wd):
        self.wd = wd

    def items_on_main_page(self):
        return self.wd.find_elements_by_css_selector('#box-most-popular .image')

