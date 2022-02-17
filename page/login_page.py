from selenium.webdriver.common.by import By


class Login_Page:
    #declaration
    __username_tb=(By.ID,"username")
    __password_tb=(By.NAME,"pwd")
    __login_btn=(By.XPATH,"//div[.='Login ']")

    #initialization
    def __init__(self,driver):
        self.driver=driver

    #utilization
    def set_username(self,un):
        self.driver.find_element(*self.__username_tb).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__password_tb).send_keys(pw)

    def click_login_button(self):
        self.driver.find_element(*self.__login_btn).click()