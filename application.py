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
        self.wd.implicitly_wait(10)

    def open_user_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart")

    def open_admin_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")

    def destroy(self):
        self.wd.quit()