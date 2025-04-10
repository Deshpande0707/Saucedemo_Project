from pageObjects.Login import LoginPage
from utilties.Logger import LogGenerator
from utilties.Readproperties import Readconfig


class Test_Login:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()


    def test_titlepage(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        if self.driver.title == "Swag Labs":
            assert True
        else:
            assert False







    def test_login01(self,setup):
        self.driver = setup
        self.log.info("start to cheking test login001")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info(" Go to this Url "+ self.url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Username(self.username)
        # self.log.info("Enter Username -->" + self.username)
        self.lp.Enter_Password(self.password)
        # self.log.info("Enter password-->" + self.password)
        self.lp.click_login()
        self.log.info("CLick to login")
        if self.lp.Login_status()==True:
            # self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\Screenshot\\test_login001.py-pass.png")
            self.lp.click_Menu()
            self.log.info("click to Menu Button")
            self.lp.click_Logout()
            self.log.info("click to Logout Button")
            assert True
            print(" condtion is True")
        else:
            # self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\Screenshot\\test_login001.py-fail.png")

            assert False


