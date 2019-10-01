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

    def clear_cart(self):
        item_count = int(self.wd.find_element_by_css_selector('#cart .content .quantity').get_attribute('textContent'))
        self.wd.find_element_by_css_selector('#cart .content .quantity').click()
        for i in range(item_count):
            wait = WebDriverWait(self.wd, 2)
            items_in_table = self.wd.find_elements_by_css_selector('td.item')
            element = wait.until(EC.presence_of_element_located((By.NAME, 'remove_cart_item')))
            element.click()
            wait.until(EC.staleness_of(items_in_table[i-2]) or not
                       EC.presence_of_element_located((By.CSS_SELECTOR, '#order-confirmation-wrapper')))

    def open_admin_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")

    def destroy(self):
        self.wd.quit()

    def admin_login(self, user, password):
        wd = self.wd
        wd.find_element_by_css_selector("[type='text']").clear()
        wd.find_element_by_css_selector("[type='text']").send_keys(user)
        wd.find_element_by_css_selector("[type='password']").send_keys(password)
        wd.find_element_by_name("login").click()

    def user_login(self, email, password):
        wd = self.wd
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()