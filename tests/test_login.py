import pytest
from pageObjects.login_page import Login_Page
from utilities.base_class import BaseClass

@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def test_login_page(self, driver):

        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        testdata = BaseClass.get_test_data()
        username = testdata["username"]
        password = testdata["password"]

        loginpage = Login_Page(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        loginpage.click_login_button()
        success = loginpage.text_fetch()
        assert "ProtoCommerce" in success
        print("Successfully logged in")

