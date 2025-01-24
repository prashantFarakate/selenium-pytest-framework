import configparser

class ConfigReader:

    VALID_SITES = ['orangehrm', 'bbc']

    def __init__(self, site='orangeHrm'):
        if site.lower() not in self.VALID_SITES:
            raise ValueError(f"Invalid site: {site}. Must be one of {self.VALID_SITES}")


        self.config = configparser.ConfigParser()
        self.config.read("configurations/config.ini")
        self.site = site.lower()

    def get_base_url(self):
        section = 'orangeHrm' if self.site == 'orangehrm' else "BBC"
        return self.config.get(section, 'BASE_URL')

    def get_username(self):
        section = 'orangeHrm' if self.site == "orangehrm" else "BBC"
        return self.config.get(section, 'USERNAME')

    def get_password(self):
        section = 'orangeHrm' if self.site == "orangehrm" else "BBC"
        return self.config.get(section, 'PASSWORD')