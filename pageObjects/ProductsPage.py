from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR, "input[type='search']")
    products = (By.XPATH, "//div[@class='product']")

    cartButton = (By.CSS_SELECTOR, ".cart-icon")
    proceedToCheckoutButton = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def get_search(self):
        return self.driver.find_element(*ProductsPage.search)

    def get_products(self):
        return self.driver.find_elements(*ProductsPage.products)

    def get_cart_button(self):
        return self.driver.find_element(*ProductsPage.cartButton)

    def get_proceed_checkout_button(self):
        self.driver.find_element(*ProductsPage.proceedToCheckoutButton).click()
        return CheckOutPage(self.driver)
