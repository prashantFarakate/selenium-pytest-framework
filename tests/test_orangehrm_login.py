import pytest
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_dashboard_page import OrangeHRMDashboardPage
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.config_reader import ConfigReader

@pytest.mark.usefixtures("setup")
class TestOrangeHrm:
    driver: WebDriver
    site : str

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.config = ConfigReader(self.site)

    def test_login(self):
        self.driver.get(self.config.get_base_url())
        login = LoginPage(self.driver)  # Pass the driver instance to LoginPage
        dashboard = OrangeHRMDashboardPage(self.driver)
        login.enter_username(self.config.get_username())
        login.enter_password(self.config.get_password())
        login.click_login()

        assert dashboard.is_on_dashboard_page(), (
            f"Login failed: Dashboard page not displayed after login. "
            f"Expected 'Dashboard' header to be visible."
        )

        dashboard.click_profile()
        dashboard.click_logout()

        assert login.is_on_login_page(), (
            f"Logout failed: Login page not displayed after logout. "
            f"Expected 'Login' header to be visible."
        )
        print("OrangeHRM Log-In Test Execution Successful")

