import pytest
from pytest_bdd import scenario
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest_bdd
import os

# def pytest_bdd_before_scenario(request, feature, scenario):
#     print(str(request.node.originalname))


# Fixtures
@pytest.fixture
def driver(request):
    print(str(request.node.originalname))
    b = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    b.implicitly_wait(10)
    yield b
    b.close()
    b.quit()
