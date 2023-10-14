import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    # request.cls.driver = driver
    yield driver
    driver.quit()

#  request.cls.driver = driver
#  yield driver
#  driver.close()
