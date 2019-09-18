from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
        self.wait = WebDriverWait(self.wd, 10)  # usage ex.: element = wait.until(EC.presence_of_element_located((By.NAME, "q")))


    def open_user_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart")

    def open_admin_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")

    def destroy(self):
        self.wd.quit()