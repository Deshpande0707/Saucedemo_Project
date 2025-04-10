from selenium.webdriver.common.by import By


class Products:

    # click_Menu_Button_XPATH = (By.XPATH,"//button[@id='react-burger-menu-btn']")
    click_Add_To_Cart_XPATH = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    click_shopping_Button_XPATH = (By.XPATH,"//a[@class='shopping_cart_link']")
    click_Continue_Shoping_XPATH = (By.XPATH,"//button[@id='continue-shopping']")
    click_Add_To_Cart1_XPATH = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    click_shopping_Button1_XPATH = (By.XPATH,"//span[@class='shopping_cart_badge']")
    click_Checkout_XPATH = (By.XPATH,"//button[@id='checkout']")
    Text_First_Name_XPATH = (By.XPATH,"//input[@id='first-name']")
    Text_last_Name = (By.XPATH,"//input[@id='last-name']")
    Text_Zip_Code = (By.XPATH,"//input[@id='postal-code']")
    click_continues = (By.XPATH,"//input[@id='continue']")
    click_Finish_Button = (By.XPATH,"//button[@id='finish']")



    def __init__(self,driver):
        self.driver = driver

    # def  Click_Menu_Button(self):
    #     self.driver.find_element(*Products.click_Menu_Button_XPATH).click()

    def  click_Add_Cart(self):
        self.driver.find_element(*Products.click_Add_To_Cart_XPATH).click()
    def  click_shopping(self):
        self.driver.find_element(*Products.click_shopping_Button_XPATH).click()

    def  click_Continue(self):
        self.driver.find_element(*Products.click_Continue_Shoping_XPATH).click()
    def  Add_TO_Cart(self):
        self.driver.find_element(*Products.click_Add_To_Cart1_XPATH).click()

    def  click_Shopinggg(self):
        self.driver.find_element(*Products.click_shopping_Button_XPATH).click()

    def click_Checkout(self):
        self.driver.find_element(*Products.click_Checkout_XPATH).click()

    def  Enter_First_Name(self,firstname):
        self.driver.find_element(*Products.Text_First_Name_XPATH).send_keys(firstname)

    def  Enter_Last_Name(self,lastname):
        self.driver.find_element(*Products.Text_last_Name).send_keys(lastname)
    def Enter_Zipcode(self,zipcode):
        self.driver.find_element(*Products.Text_Zip_Code).send_keys(zipcode)

    def click_Continues(self):
        self.driver.find_element(*Products.click_continues).click()

    def click_Finish(self):
        self.driver.find_element(*Products.click_Finish_Button).click()




