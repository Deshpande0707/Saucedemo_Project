import pytest

from pageObjects.Login import LoginPage
from pageObjects.Productss import Products
from utilties.Logger import LogGenerator
from utilties.Readproperties import Readconfig


class Test_AddProduct:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_addpro(self,setup):
        self.driver = setup
        self.log.info("test case addpro is started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info(" go to this Url-->" + self.url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Username(self.username)
        self.log.info("Enter Username-->"+ self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter password -->" + self.password)
        self.lp.click_login()
        self.log.info("Enter login-->")
        self.pa = Products(self.driver)
        # self.pa.Click_Menu_Button()
        self.pa.click_Add_Cart()
        self.log.info("add to cart product")
        self.pa.click_shopping()
        self.log.info("click to shoping")
        self.pa.click_Continue()
        self.log.info("click to the continue")
        self.pa.Add_TO_Cart()
        self.log.info(" add to the cart")
        self.pa.click_Shopinggg()
        self.log.info("click to the continue")
        self.pa.click_Checkout()
        self.log.info("click to the cheakout")
        self.pa.Enter_First_Name("Mukesh")
        self.log.info("Enter the first name")
        self.pa.Enter_Last_Name("Deshpande")
        self.log.info("Enter the last name")
        self.pa.Enter_Zipcode("458874")
        self.log.info("Enter the zipcode")
        self.pa.click_Continues()
        self.log.info("Enter the click continue")
        self.pa.click_Finish()
        self.log.info("click to the finish")





