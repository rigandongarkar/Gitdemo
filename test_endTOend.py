from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckoutPage


# updating from x user

class TestOne(BaseClass):
    def test_EndtoEnd(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckoutPage(self.driver)
        products = checkOutPage.checkoutItems()

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element_by_xpath("div[2]/button").click()

        checkOutPage.checkoutButton().click()  # checkout proceed
        checkOutPage.checkoutFinalButton().click()  # Checkout Final

        confirmPage_Obj = ConfirmPage(self.driver)
        confirmPage_Obj.addressDropdown().send_keys("ind")
        # wait = WebDriverWait(self.driver, 8)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        log.info("Country Selection")
        self.VerifyLinkPresence("India")  # Optimized in BaseClass
        confirmPage_Obj.addressSelection().click()
        confirmPage_Obj.purchaseButton().click()
        successText = confirmPage_Obj.successText().text
        log.info("Success Text : " + successText)

        assert "Success" in successText

        self.driver.get_screenshot_as_file("screenshot1.png")  # method to get screenshot
