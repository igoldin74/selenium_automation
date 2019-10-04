from selenium.webdriver.support.wait import WebDriverWait
from helpers.get_new_window_handler import GetWindowHandler

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
        # passing anonymous lambda function:
        # new_window_id = wait.until(lambda d: app.get_new_window_id(old_windows))
        new_window_id = wait.until(GetWindowHandler(old_windows))  # using helper class
        app.wd.switch_to_window(new_window_id)
        app.wd.close()
        app.wd.switch_to_window(active_window)
