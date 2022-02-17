from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Enter_Time_Track_Page:

    __ett_element=(By.XPATH,"//td[.='Enter Time-Track']")

    def __init__(self,driver):
        self.driver=driver

    def verify_ett_page_is_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__ett_element))
            print('Home page is displayed')
            return True
        except:
            print('Home page is NOT displayed')
            return False