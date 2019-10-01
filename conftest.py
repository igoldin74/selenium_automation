import pytest
import json
import os.path
from application import Application


fixture = None

@pytest.fixture
def app():
    global fixture
    browser = "chrome"
    if fixture is None or fixture.is_not_valid():
        fixture = Application(browser=browser)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
