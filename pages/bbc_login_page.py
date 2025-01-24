from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BBCLoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)

        # Locators
        self.username_input = (By.ID, "user-identifier-input")
        self.submit_button = (By.ID, "submit-button")
        self.password_input = (By.NAME, "password")
        self.signin_page_signin_button = (By.ID, "submit-button")
        self.sign_out_message = (By.XPATH, '//*[@id="app-container"]/div/div/div/h1/span')

    def enter_username(self, username):
        self.send_keys_to_element(self.username_input, username)

    def click_submit_button(self):
        self.click_element(self.submit_button)

    def enter_password(self, password):
        self.send_keys_to_element(self.password_input, password)

    def click_signin_page_signin(self):
        self.click_element(self.signin_page_signin_button)

    def is_sign_out_message_displayed(self):
        try:
            message = self.get_element_text(self.sign_out_message)
            return message == "You've signed out, sorry to see you go."
        except Exception as e:
            print(f"Error validating sign-out message: {e}")
            return False



