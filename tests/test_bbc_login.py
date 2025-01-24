import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.bbc_login_page import BBCLoginPage
from pages.bbc_home_page import BBCHomePage
from utilities.config_reader import ConfigReader

@pytest.mark.usefixtures("setup")
class TestBBCLogin:
    driver : WebDriver
    site: str

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.config = ConfigReader(self.site)

    def test_bbc_login(self):
        self.driver.get(self.config.get_base_url())
        signin = BBCLoginPage(self.driver)
        homepage = BBCHomePage(self.driver)
        # signin
        homepage.click_homepage_signin()
        signin.enter_username(self.config.get_username())
        signin.click_submit_button()
        signin.enter_password(self.config.get_password())
        signin.click_signin_page_signin()

        assert self.driver.title == "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio"
        assert homepage.is_your_account_button_visible(), "Login failed: 'Your Account' button not visible."

        # sign out
        homepage.click_your_account_button()
        homepage.click_sign_out_button()

        assert signin.is_sign_out_message_displayed(), "Sign out failed: Sign-out message not displayed or incorrect."
        print("BBC Log-In Test Execution Successful")

