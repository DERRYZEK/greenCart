from selenium.webdriver.common.by import By

from pageObjects.ProductsPage import ProductsPage
from utilities.BaseClass import BaseClass


class TestGreenCart(BaseClass):

    def test_green_cart(self):
        log = self.getLogger()

        productsPage = ProductsPage(self.driver)

        productsPage.get_search().send_keys("ber")
        products = productsPage.get_products()

        i = -1
        for product in products:
            i = i + 1
            product.find_element(By.XPATH, "div[3]/button").click()

        productsPage.get_cart_button().click()
        checkoutPage = productsPage.get_proceed_checkout_button()

        #checkoutPage.get
