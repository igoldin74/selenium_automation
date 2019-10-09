

def test_for_browser_log_msg(app):
    app.open_admin_login_page()
    app.admin_login(user="admin",password="admin" )
    app.wd.find_elements_by_css_selector('#app-')[1].click()
    app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')[1].click()
    app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')[2].click()
    rows = app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')
    for i in range(len(rows)):
        app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')[2].click()
        rows = app.wd.find_elements_by_css_selector('.row td:nth-child(3) a')
        rows[i].click()
        app.wd.back()
        logs = app.wd.get_log('browser')
        for l in logs:
            assert l is None
