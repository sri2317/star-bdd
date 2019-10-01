import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import json
from tests.pageobjects.homescreen import HomeScreen
from tests.pageobjects.resultsscreen import ResultsScreen

scenarios('../features/web.feature')


# Given Steps
@given('the wikipedia home page is displayed')
def navigate_to_app_homepage(driver):
    data = json.loads(open('star.json').read())
    driver.get(str(data['URLS']['QA']))


# When Steps
@when(parsers.parse('the user searches for "<name>"'))
def enter_name_in_searchbox(driver, name):
    search = HomeScreen(driver)
    search.enter_text_in_searchbox(name)


# Then Steps
@then(parsers.parse('results are shown for "<name>"'))
def validate_header_value(driver, name):
    header = ResultsScreen(driver)
    header.verify_header_text(name)
    print('this is a print statement in the test_web file')
