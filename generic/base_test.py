import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
# driver---->local variable
# self.driver--->global variable

class BaseTest:

    @pytest.fixture(autouse=True)
    def open_close_app(self):
        # create object of Properties class
        p_file = Properties()

        # open the properties file and load it
        p_file.load(open("config.properties"))

        self.xl_path = p_file['XLPATH']

        # open the browser
        use_grid=p_file['USEGRID']

        if use_grid=='YES':
            print("Using Selenium Grid")
            grid_url=p_file['GRIDURL']
            browser=p_file['BROWSER']
            print("Browser is:", browser)
            if browser=='chrome':
                browser_option = ChromeOptions()
            else:
                browser_option = FirefoxOptions()
            self.driver = webdriver.Remote(command_executor=grid_url, options=browser_option)

        else:
            print("Using Local System")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




        # maximize the browser
        self.driver.maximize_window()

        # implicit wait
        ito = p_file['ITO']  # get ITO from properties file
        self.driver.implicitly_wait(ito)

        # explicit wait
        eto = p_file['ETO']  # get ETO from properties file
        self.wait = WebDriverWait(self.driver, eto)

        # enter the URL
        url = p_file['URL']  # get URL from properties file
        self.driver.get(url)

        yield  # Go,run the test and come back

        # close the browser
        self.driver.close()
