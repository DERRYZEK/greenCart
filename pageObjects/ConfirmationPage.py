from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    countrySelector = (By.XPATH, "//div/select")
    termCheckbox = (By.CSS_SELECTOR, ".chkAgree")
    proceedButton = (By.XPATH, "//button")
