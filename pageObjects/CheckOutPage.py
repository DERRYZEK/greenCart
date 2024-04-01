from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutProducts = (By.XPATH, ("//tbody/tr/td[2]/p"))
    itemPrices = (By.XPATH, "//tbody/tr/td[5]")
    promoCodeInput = (By.CSS_SELECTOR, ".promoCode")
    promoButton = (By.CSS_SELECTOR, ".promoBtn")
    promoInfo = (By.CSS_SELECTOR, ".promoInfo")
    totalItemsAmount = (By.CSS_SELECTOR, ".totAmt")
    totalAmountAfterDiscount = (By.CSS_SELECTOR, ".discountAmt")
    placeOrderButton = (By.XPATH, "//button[text()='Place Order']")

    def get_check_out_products(self):
        return self.driver.find_elements(*CheckOutPage.checkoutProducts)

    def get_item_prices(self):
        return self.driver.find_elements(*CheckOutPage.itemPrices)

    def get_promo_code_input(self):
        return self.driver.find_element(*CheckOutPage.promoCodeInput)

    def get_promo_button(self):
        return self.driver.find_element(*CheckOutPage.promoButton)

    def get_promo_info(self):
        return self.driver.find_element(*CheckOutPage.promoInfo)

    def get_total_item_amount(self):
        return self.driver.find_element(*CheckOutPage.totalItemsAmount)

    def get_total_amount_after_discount(self):
        return self.driver.find_element(*CheckOutPage.totalAmountAfterDiscount)

    def get_place_order_button(self):
        self.driver.find_element(*CheckOutPage.placeOrderButton).click()
        return ConfirmationPage(self.driver)
