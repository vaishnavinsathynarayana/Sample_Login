import pytest
from selenium import webdriver
import logging

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO, filename="test_log.log", filemode="a",format="%(asctime)s -%(message)s")
    logging.info("Starting tests")
@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()
