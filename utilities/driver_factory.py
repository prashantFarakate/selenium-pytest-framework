from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class DriverFactory:
    @staticmethod
    def get_driver(browser_type="chrome", headless=False):
        browser_type = browser_type.lower()

        if browser_type == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            return webdriver.Chrome(options = options)

        elif browser_type == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            return webdriver.Edge(options = options)

        elif browser_type == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            return webdriver.Firefox(options = options)
        else:
            raise ValueError(f"Browser type {browser_type} not supported")

