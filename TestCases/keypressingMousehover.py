import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/Users/Hp/Desktop/New nani/chromedriver.exe")
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fyour-account%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("9550099259")

act = ActionChains(driver)
act.send_keys(Keys.ENTER).perform()


driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("madhan@8080")

act.send_keys(Keys.ENTER).perform()

time.sleep(3)

        # identify elemen
m=driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
        # hover over element
act.move_to_element(m).perform()

driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()
driver.close()


