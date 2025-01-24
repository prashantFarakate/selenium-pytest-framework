import pytest
from utilities.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption("--site", action="store", default="orangehrm",
                     help="Website to test (orangehrm/bbc)")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run the test : chrome/firefox/edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run Browser in Headless mode")

@pytest.fixture(scope="class")
def setup(request):
    site = request.config.getoption("--site").lower()
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser, headless)

    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver # Assign driver to the test class
    request.cls.site = site     # Make site available to test class

    yield driver  # Yield the driver instance to the test
    driver.close()
    driver.quit()
