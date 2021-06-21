from selenium import webdriver
import pytest
import time

class TestWebApplication():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Hp/Desktop/New nani/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.mark.regression
    def test_prod(self,setup):
        self.driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
        self.driver.find_element_by_xpath("//input[@id='ap_email']").clear()
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("9550099259")
        self.driver.find_element_by_xpath("//input[@id='continue']")









