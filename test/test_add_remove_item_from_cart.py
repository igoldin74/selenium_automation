from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_cart_add_remove_item(app):
    app.user_login(email='user@mail.com', password='password')
    for i in range(3):

        pass