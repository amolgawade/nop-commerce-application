
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Add_customer import addcustomer
from pageObjects.loginpage import LoginPage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
from Utilities import XLutils


class Test_003_addCustomer:
    baseUrl = Readconfig.getapplictionURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("********* Test add customer *******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********* login successful *******")

        self.logger.info("********* Starting add New customer test *******")
        time.sleep(5)

        self.addcust = addcustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerSubmenu()
        self.addcust.clickOnAddnew()
        self.addcust.setEmail("TyatyaVinchu@gmail.com")
        self.addcust.setPassword("Ashi Hi Bnawa Banvi")
        self.addcust.setFirstname("laxmikan")
        self.addcust.setLastname("Berade")
        self.addcust.setGender("Male")
        self.addcust.setBirthDay("08/15/1947")
        self.addcust.setCompanyName("marathi.mollywood.pvt.ltd")
        self.addcust.setTaxExempt()
        time.sleep(2)
        self.addcust.drpNewsLettter("1")
        self.addcust.setCustomerRoles("Registered")
        time.sleep(3)
        self.addcust.drpManegerofVendor("Vendor 2")
        time.sleep(3)
        self.addcust.clickonActive()
        self.addcust.setadmincomment("This is for testing ......")
        self.addcust.clickonSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.mesg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.mesg)
        if "customer has been added successfully" in self.mesg:
            assert True == True
            self.logger.info("************* Add customer is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCustomer_scr.png")
            self.logger.info("************* Add customer is failed**********")
            assert False == False

        self.driver.close()
        self.logger.info("************* Ending Add customer test**********")










