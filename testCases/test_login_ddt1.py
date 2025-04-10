# from pageObjects.LoginPage import Login
# # from utilities.Logger import LogGenerator
# from utilities.Readproperties import Readconfig
import time

import openpyxl
import pytest
from pageObjects.Login import LoginPage
from utilties import XLutils
from utilties.Readproperties import Readconfig
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver.support.wait import WebDriverWait






class Test_Login_DDT:

    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    # log = LogGenerator.loggen()
    path = "C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\testCases\\TestData\\Logindata (2).xlsx"


    def test_login_ddt_05(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getrowCount(self.path,'Sheet1')
        login_status=[]
        for r in range(2, self.rows+1):
            self.Username = XLutils.readData(self.path,'Sheet1',r,1)
            self.Password = XLutils.readData(self.path,'Sheet1',r,2)
            # self.Exp_result = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.Enter_Username(self.Username)
            self.lp.Enter_Password(self.Password)
            self.lp.click_login()
            login_status=[]
            if self.lp.Login_status()==True:
                # if self.Exp_result == "Pass":
                    self.lp.click_Menu()
                    self.lp.click_Logout()
                    login_status.append("Pass")
                    XLutils.writeData(self.path,'Sheet1',r,4,"Pass")

            else:
                    login_status.append("Fail")
                    XLutils.writeData(self.path,'Sheet1',r,4,"Fail")

        print(login_status)
        if "Fail" not in login_status:
            assert True
        else:
            assert False






















































    #
    # def test_login_params_003(self,setup,getDataForLogin):
    #     self.log.info("Opeing Browser")
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.log.info("Going to url")
    #     self.lp = login(self.driver)
    #     self.lp.Enter_UserName(getDataForLogin[0])
    #     self.log.info("Enter username-->" + getDataForLogin[0])
    #     self.lp.Enter_Password(getDataForLogin[1])
    #     self.log.info("Enter password-->"+ getDataForLogin[1])
    #     self.lp.Click_Login()
    #     self.log.info("click the login")
    #     login_status=[]
    #     if self.lp.Login_Status()==True:
    #         if getDataForLogin[2]=="Pass":
    #             login_status.append("Pass")
    #             self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-pass.png")
    #             self.lp.Click_MenuButton()
    #             self.log.info("click Menu Button")
    #             self.lp.Click_Logout()
    #             self.log.info("Click logout Button")
    #         elif getDataForLogin[2]=="Fail":
    #             login_status.append("Fail")
    #             self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
    #             self.lp.Click_MenuButton()
    #             self.log.info("CLick menu botton")
    #             self.lp.Click_Logout()
    #             self.log.info("click logout")
    #     else:
    #         if getDataForLogin[2]=="Fail":
    #             login_status.append("Pass")
    #             self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
    #         elif getDataForLogin[2] =="Pass":
    #             login_status.append("Fail")
    #             self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
    #     print(login_status)
    #
    #     if "Fail" not in login_status:
    #         self.log.info("test_login_params_003 is passed")
    #         assert True
    #     else:
    #         self.log.info("test_login_params is failed")
    #     self.driver.close()
    #
