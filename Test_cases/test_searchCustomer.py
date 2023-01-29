
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Add_customer import addcustomer
from pageObjects.loginpage import LoginPage
from pageObjects.SearchCustomerpage import searchCustomer
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
from Utilities import XLutils


class Test_004_searchCustomer_Byemail:
    baseUrl = Readconfig.getapplictionURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_searchResultByemail(self,setup):
        self.logger.info("********* Test search customer by email *******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********* login successful *******")

        self.logger.info("********* Starting searching customer test *******")
        time.sleep(5)

        self.addcust = addcustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerSubmenu()

        self.logger.info("************* searching customer by emailID **********")

        searchcust = searchCustomer(self.driver)
        searchcust.setEmail("steve_gates@nopCommerce.com")
        searchcust.clickSerch()
        time.sleep(5)
        status = searchcust.searchByEmail('steve_gates@nopCommerce.com')
        self.driver.close()
        assert True == status
        self.logger.info("******* test search finished ******")

