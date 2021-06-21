

class AmazonProduct:

    textbox_email_xpath="//input[@id='ap_email']"
    linktext_continue_xpath="//input[@id='continue']"
    textbox_password_xpath="//input[@id='ap_password']"
    btn_singin_xpath="//input[@id='signInSubmit']"
    textsearchbox_product_xpath="//input[@id='twotabsearchtextbox']"
    btn_seach_class="nav-input nav-progressive-attribute"
    radiobtn_product_xpath="//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/span[1]/a[1]/div[1]/label[1]/i[1]"
    linktext_newmobile_xpath="//div[contains(text(),'New Apple iPhone 12 Mini (128GB) - Black')]"
    linktext_customerreview_xpath="//a[@id='a-autoid-47-announce']"
    linktext_logout_xpath="//span[contains(text(),'Sign Out')]"

    def __init__(self,driver):
        self.driver=driver

    def emailLogIN(self,mobilenumber):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(mobilenumber)

    def clickBtnContinue(self):
        self.driver.find_element_by_xpath(self.linktext_continue_xpath).click()

    def passwordLogIn(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickBtnSingin(self):
        self.driver.find_element_by_xpath(self.btn_singin_xpath).click()

    def searchBox(self,iphone):
        self.driver.find_element_by_xpath(self.textsearchbox_product_xpath).clear()
        self.driver.find_element_by_xpath(self.textsearchbox_product_xpath).send_keys(iphone)

    def clickonsignout(self):
        self.driver.find_element_by_xpath(self.linktext_logout_xpath).click()



    def clickBtnradio(self):
        self.driver.find_element_by_id(self.radiobtn_product_xpath).click()



    def ClickproductnewMobile(self):
        self.driver.find_element_by_xpath(self.linktext_newmobile_xpath).click

    def ClickCustomerreview(self):
        self.driver.find_element_by_xpath (self.linktext_customerreview_xpath).click

