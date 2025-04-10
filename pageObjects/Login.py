from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException , NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Text_Username_XPATH = (By.XPATH,"//input[@id='user-name']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='password']")
    click_Login_XPATH = (By.XPATH,"//input[@id='login-button']")
    click_Menu_XPATH = (By.XPATH,"//button[@id='react-burger-menu-btn']")
    click_logout_XPATH = (By.XPATH,"//a[@id='logout_sidebar_link']")



    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)


    def  Enter_Username(self,username):
        self.driver.find_element(*LoginPage.Text_Username_XPATH).clear()
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Username_XPATH))
        self.driver.find_element(*LoginPage.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).clear()
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Password_XPATH))
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.click_Login_XPATH).click()
    def Login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.click_Menu_XPATH))
            self.driver.find_element(*LoginPage.click_Menu_XPATH)
            return True
        except (NoSuchElementException,TimeoutException):
            return False
    def click_Menu(self):
        self.driver.find_element(*LoginPage.click_Menu_XPATH).click()

    def click_Logout(self):
        self.driver.find_element(*LoginPage.click_logout_XPATH).click()

    #
    # def Title(self):
    #     self.driver.implicitly_wait(10)
    #     try:
    #         title = self.driver.title
    #         return True
    #     except Ec:
    #         title = self.driver.title
    #         return False