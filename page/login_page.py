from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Login_Page:
    #declaration
    __username_tb=(By.ID,"username")
    __password_tb=(By.NAME,"pwd")
    __login_btn=(By.XPATH,"//div[.='Login ']")
    __err_msg=(By.XPATH,"//span[contains(.,'invalid')]")

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

    def verify_err_msg_is_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__err_msg))
            print('Err Msg is displayed')
            msg=self.driver.find_element(*self.__err_msg).text
            print(msg)
            return True
        except:
            print('Err Msg is NOT displayed')
            return False