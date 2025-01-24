from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrangeHRMDashboardPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        # Locators
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.profile_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span')
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def is_on_dashboard_page(self):
        return self.get_element_text(self.dashboard_header)

    def click_profile(self):
        self.click_element(self.profile_button)

    def click_logout(self):
        self.click_element(self.logout_button)


