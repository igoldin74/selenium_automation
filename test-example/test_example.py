import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_yandex(driver):
    driver.get("http://www.yandex.ru")
    WebDriverWait(driver, 10).until(EC.title_is("Яндекс"))

