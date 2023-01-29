import time

import pytest
from selenium import webdriver
from pageObjects.loginpage import LoginPage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
from Utilities import XLutils

class Test_002_DDT_login:
    path = ".//Testdata/login_data.xlsx"
    baseUrl = Readconfig.getapplictionURL()

    logger = LogGen.loggen()


    def test_login_DDT(self, setup):
        self.logger.info("************ Test_002_DDT_login ************")
        self.logger.info("************ verifying login DDT test ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getrowsCount(self.path, "Sheet1")
        print("no of rows :-", self.rows)

        list_status =[]
        for r in range(2, self.rows+1):
            self.user = XLutils.readData(self.path,"Sheet1", r, 1)
            self.password = XLutils.readData(self.path,"Sheet1", r, 2)
            self.exp = XLutils.readData(self.path,"Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"


            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("****passed***")
                    self.lp.clicklogout();
                    list_status.append("passed")
                elif self.exp == "fail":
                     self.logger.info("****failed***")
                     self.lp.clicklogout();
                     list_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("****failed")
                    list_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("****passed")
                    time.sleep(3)
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("**** login ddt test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** login ddt test failed ***")
            assert False


