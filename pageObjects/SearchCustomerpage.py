import time
from selenium.webdriver.support.select import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class searchCustomer:

    txtbox_email_xpath = "//input[@id='SearchEmail']"
    txtbox_fname_xpath = "//input[@id='SearchFirstName']"
    txtbox_lname_xpath = "//input[@id='SearchLastName']"
    button_serach_xpath = "//button[@id='search-customers']"

    table_xpath ="//table[@id='customers-grid']"

    table_column_xpath = "//table/tbody/tr[1]/td"
    table_row_xpath = "//tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def setName(self,name):
        self.driver.find_element(By.XPATH,self.txtbox_fname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbox_fname_xpath).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtbox_lname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbox_lname_xpath).send_keys(lname)

    def clickSerch(self):
        self.driver.find_element(By.XPATH,self.button_serach_xpath).click()

    def getRowNo(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def getColumnNo(self):
        return len(self.driver.find_elements(By.XPATH,self.table_column_xpath))

    def searchByEmail(self, email):
        flag = False
        for r in range(1, self.getRowNo()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchByname(self, Name):
        flag = False
        for r in range(1, self.getRowNo()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag







