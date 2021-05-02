import pytest

from TestData.testData_HomePage import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("firstname print")
        homepage.getName().send_keys(getData['First Name'])
        # log.info(homepage.getName().get_attribute())
        log.info("email print")
        homepage.getEmail().send_keys(getData['Email'])
        homepage.getPasswd().send_keys(getData['Password'])
        homepage.getExample().click()
        homepage.getButton().click()

        message = homepage.getText().text

        assert "Success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Raj", "raj@mail.com", "1234"), ("Sam", "sam@mail.com", "4321")])
    @pytest.fixture(params=HomePageData.getTestData("tc3"))
    def getData(self, request):
        return request.param
