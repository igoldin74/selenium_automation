from selenium import webdriver


class Application:
    def __init__(self, browser):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart")

    def destroy(self):
        self.wd.quit()