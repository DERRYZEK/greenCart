
from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    countrySelector = (By.XPATH, "//div/select")
    termCheckbox = (By.CSS_SELECTOR, ".chkAgree")
    proceedButton = (By.XPATH, "//button")

    def get_country(self):
        return self.driver.find_element(*ConfirmationPage.countrySelector)

    def get_click_checkBox(self):
        return self.driver.find_element(*ConfirmationPage.termCheckbox)

    def get_proceed_button(self):
        return self.driver.find_element(*ConfirmationPage.proceedButton)
