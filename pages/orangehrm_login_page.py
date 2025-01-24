from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage): # Inherit from BasePage

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)  # Initialize the parent class

        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[text()=' Login ']")
        self.login_header = (By.XPATH, "//h5[text()='Login']")

    def enter_username(self, username):
        self.send_keys_to_element(self.username_input, username)

    def enter_password(self, password):
        self.send_keys_to_element(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def is_on_login_page(self):
        return self.get_element_text(self.login_header)
