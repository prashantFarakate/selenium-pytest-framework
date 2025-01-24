# import pytest
# from selenium import webdriver
#
# def pytest_adoption(parser):
#     parser.adoption("--site", action="store", default="orangehrm",
#     help="Website to test (orangehrm/bbc)")
#
# @pytest.fixture(scope="session")
# def site(request):
#     return request.config.getoption("--site").lower()
#
# @pytest.fixture(scope="class")
# def setup(request, site):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     request.cls.driver = driver # Assign driver to the class
#     request.cls.site = site     # Make site available to test class
#
#     yield driver  # Yield the driver instance to the test
#     driver.close()
#     driver.quit()
