from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver(request):
    print("setup")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    def quit_browser():
        driver.quit()
    request.addfinalizer(quit_browser)

    return driver
