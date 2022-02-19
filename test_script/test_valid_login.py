import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.enter_time_track_page import Enter_Time_Track_Page
from page.login_page import Login_Page


class Test_Valid_Login(BaseTest):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
#get Data from excel file
        un=Excel.get_data(self.xl_path,"ValidLogin",2,1)
        pw = Excel.get_data(self.xl_path, "ValidLogin", 2, 2)
# 1.	Enter valid username- admin
        login_page=Login_Page(self.driver)
        login_page.set_username(un)

# 2.	Enter valid password-manager
        login_page.set_password(pw)

# 3.	Click login button
        login_page.click_login_button()

# 4.	Verify that home page is displayed
        ett_page=Enter_Time_Track_Page(self.driver)
        result=ett_page.verify_ett_page_is_displayed(self.wait)
        assert result

