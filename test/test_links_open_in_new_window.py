from random import randrange
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_edit_link_open_in_new_window(app):
    active_window = app.wd.current_window_handle
    old_windows = app.wd.window_handles
    wait = WebDriverWait(app.wd, 5)
    app.open_admin_login_page()
    app.admin_login(user='admin', password='admin')
    app.wd.find_elements_by_css_selector('#app-')[2].click()
    country_list = app.wd.find_elements_by_css_selector('tbody tr td:nth-child(5) a')
    country_list[0].click()
    ext_links = app.wd.find_elements_by_css_selector('#content tbody tr td a i')
    for i, ext_links in enumerate(ext_links):
        ext_links = app.wd.find_elements_by_css_selector('#content tbody tr td a i')
        ext_links[i].click()
        new_window_id = wait.until(app.get_new_window_id(old_windows))
        app.wd.switch_to.window(new_window_id)
        app.wd.close(new_window_id)
        app.wd.switch_to_window(active_window)
