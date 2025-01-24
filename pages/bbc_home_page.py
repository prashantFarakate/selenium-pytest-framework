from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BBCHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)

        # Locators
        self.homepage_signin_button = (By.XPATH, "//span[normalize-space()='Sign In']")
        self.your_account_button = (By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/button')
        self.sign_out_button = (By.XPATH, '/html/body/div[2]/div/header/div/div[3]/div/div/div/div[3]/a')

    def click_homepage_signin(self):
        self.click_element(self.homepage_signin_button)

    def is_your_account_button_visible(self):
        try:
            return self.is_element_visible(self.your_account_button)
        except Exception as e:
            print(f"Error validating 'Your Account' button visibility: {e}")
            return False

    def click_your_account_button(self):
        self.click_element(self.your_account_button)

    def click_sign_out_button(self):
        self.click_element(self.sign_out_button)