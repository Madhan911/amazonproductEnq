from selenium import webdriver

import pytest
import time
from PageObjects.AmazonProd import AmazonProduct
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller

class TestProd:




    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Hp/Desktop/New nani/chromedriver.exe")
        self.driver.maximize_window()



    def test_prod(self,setup):

        baseURL="https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1"

        mobilenumber="919550099259"

        password="madhan@8080"
        iphone="iphone 12 pro max phone case"



        self.driver.get(baseURL)
        self.driver.maximize_window()

        self.sp =AmazonProduct(self.driver)

        self.sp.emailLogIN(mobilenumber)
        self.sp.clickBtnContinue()

        self.sp.passwordLogIn(password)
        self.sp.clickBtnSingin()

        a = ActionChains(self.driver)
        # identify element
        m = self.driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
        # hover over element
        a.move_to_element(m).perform()

        self.sp.clickonsignout()



        self.driver.close()




        '''self.sp.ClickCustomerreview()

        self.msg = self.driver.find_element_by_tag_name("body").text

        if "We apologize but this account has not met the minimum eligibility requirements to write a review. If you would like to learn more about our eligibility requirements, please see our community guidelines." in self.msg:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testprod.png")
            assert False

        self.driver.close() '''



