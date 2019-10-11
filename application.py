from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.main_page import MainPage
from helpers.item_page import ItemPage
from random import randrange

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
        self.wait = WebDriverWait(self.wd, 5)  # usage ex.: element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        self.main_page = MainPage(self.wd)
        self.item_page = ItemPage(self.wd)

    def open_user_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart")

    def clear_cart(self):
        wait = WebDriverWait(self.wd, 2)
        self.wd.find_element_by_css_selector('#cart .content .quantity').click()
        items_in_table = self.wd.find_elements_by_css_selector('td.item')
        for i in range(len(items_in_table)):
            element = wait.until(EC.presence_of_element_located((By.NAME, 'remove_cart_item')))
            element.click()
            wait.until(EC.staleness_of(items_in_table[i]))

    def open_admin_login_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")

    def get_new_window_id(self, original_windows):
        wd = self.wd
        new_windows = set(wd.window_handles)
        diff = list(set(new_windows) - set(original_windows))
        if len(diff) == 1:
            return diff[0]
        else:
            return False

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

    def open_random_item_page(self):
        items = self.main_page.items_on_main_page()
        items[randrange(len(items))].click()
        return self

    def add_item_to_cart(self, qty, size_idx):
        for i in range(qty):
            self.open_user_login_page()
            self.open_random_item_page()
            self.item_page.select_size(size_idx)
            self.item_page.click_add_to_cart_button()
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart .content .quantity'), str(i + 1)))

    def cart_item_count(self):
        return int(self.item_page.cart().get_attribute('textContent'))

