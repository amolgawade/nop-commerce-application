import pytest
from selenium import webdriver
from pageObjects.loginpage import LoginPage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen


class Test_001_login:
    baseUrl = Readconfig.getapplictionURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_homepage_title(self, setup):

        self.logger.info("************ Test_001_login ************")
        self.logger.info("************ Home page title test ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("************ Home page title is matched/pass ************")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homepage_title.png")
            self.logger.info("************ Home page title is  not matched/fail ************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("************ login test ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************ login test pass ************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_login.png")
            self.logger.info("************ login test fail ************")
            self.driver.close()
            assert False



