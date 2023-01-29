import time
from select import select

from selenium.webdriver.support.select import Select

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class addcustomer:

    link_customerMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    link_cust_submenu_xpath = "(//p[contains(text(),'Customers')])[2]"
    button_addNew_xpath = "//a[@class='btn btn-primary']"

    textbox_email_xpath = "//input[@id='Email']"
    textbox_passsword_xpath = "//input[@id='Password']"
    textbox_fristName_xpath = "//input[@id='FirstName']"
    textbox_lastname_xpath = "//input[@id='LastName']"

    but_radio_male_xpath = "//input[@id='Gender_Male']"
    but_radio_female_xpath = "//input[@id='Gender_Female']"

    textbox_dBirth_xpath = "//input[@id='DateOfBirth']"
    textbox_company_xpath = "//input[@id='Company']"

    checkbox_taxExempt_xpath = "//input[@id='IsTaxExempt']"

    textbox_newsLetter_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    listItem_Test_store_xpath = "//option[normalize-space()='Test store 2']"
    listItem_Your_store_xpath = "//option[normalize-space()='Your store name']"

    textbox_customerRole_xpath = "(//div[@role='listbox'])[2]"
    listItem_vendor_xpath = "//option[normalize-space()='Vendors']"
    listItem_Registered_xpath = "//option[normalize-space()='Registered']"
    listItem_Administrators_xpath = "//option[normalize-space()='Administrators']"
    listItem_guest_xpath = "//option[@value='4']"

    drp_manegerofvendor_xpath = "//select[@id='VendorId']"
    listItem_maneofvend1_xpath = "//option[normalize-space()='Vendor 1']"
    listItem_maneofvend2_xpath = "//option[normalize-space()='Vendor 2']"

    checkbox_active_xpath = "//input[@id='Active']"

    textbox_Admincomment_xpath = "//textarea[@id='AdminComment']"

    butt_save_xpath = "//button[@name='save']"
    butt_save_conti_xpath = "//button[@name='save-continue']"
    link_customerlist_xpath = "//a[normalize-space()='back to customer list']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customerMenu_xpath).click()

    def clickOnCustomerSubmenu(self):
        self.driver.find_element(By.XPATH, self.link_cust_submenu_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.button_addNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self,passw):
        self.driver.find_element(By.XPATH, self.textbox_passsword_xpath).send_keys(passw)

    def setFirstname(self, name):
        self.driver.find_element(By.XPATH, self.textbox_fristName_xpath).send_keys(name)

    def setLastname(self,last):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(last)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.but_radio_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.but_radio_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.but_radio_male_xpath).click()

    def setBirthDay(self,date):
        self.driver.find_element(By.XPATH, self.textbox_dBirth_xpath).send_keys(date)

    def setCompanyName(self,cname):
        self.driver.find_element(By.XPATH, self.textbox_company_xpath).send_keys(cname)

    def setTaxExempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_taxExempt_xpath).click()

    def drpNewsLettter(self, value):
        self.driver.find_element(By.XPATH, "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div").click()
        self.driver.implicitly_wait(3)
        drp = Select(self.driver.find_element(By.XPATH, self.textbox_newsLetter_xpath))
        self.driver.implicitly_wait(3)
        drp.select_by_value(value)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.textbox_customerRole_xpath).click()
        time.sleep(3)
        if role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Administrators_xpath)
        elif role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Registered_xpath)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_vendor_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_guest_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH, "//option[@value='4']")

        self.driver.execute_script("arguments[0].click();", self.listItem)

    def drpManegerofVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_manegerofvendor_xpath))
        drp.select_by_visible_text(value)


    def clickonActive(self):
        self.driver.find_element(By.XPATH,self.checkbox_active_xpath).click()

    def setadmincomment(self,content):
        self.driver.find_element(By.XPATH,self.textbox_Admincomment_xpath).send_keys(content)

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.butt_save_xpath).click()

    def clickOnBackToCusList(self):
        self.driver.find_element(By.XPATH,self.link_customerlist_xpath).click()





