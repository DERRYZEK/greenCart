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

        checkOutProducts = checkoutPage.get_check_out_products()

        for checkoutProduct in checkOutProducts:
            checkoutPage.actualCheckoutProductList.append(checkoutProduct.text)

        assert checkoutPage.actualCheckoutProductList == checkoutPage.checkoutProductList

        itemPrices = checkoutPage.get_item_prices()

        for itemPrice in itemPrices:
            checkoutPage.totalItemPrice = checkoutPage.totalItemPrice + float(itemPrice.text)

        assert checkoutPage.totalItemPrice == float(checkoutPage.get_actual_total_item_amount().text)

        checkoutPage.get_promo_code_input().send_keys("rahulshettyacademy")

        checkoutPage.get_promo_button().click()
        self.verifyElementPresent(".promoInfo")
        assert checkoutPage.get_promo_info().text == "Code applied ..!"

        assert float(checkoutPage.get_total_amount_after_discount().text) < float(
            checkoutPage.get_actual_total_item_amount().text)

        confirmPage = checkoutPage.get_place_order_button()

        self.selectOptionByText(confirmPage.get_country(), "Ghana")

        confirmPage.get_click_checkBox().click()
        confirmPage.get_proceed_button().click()

