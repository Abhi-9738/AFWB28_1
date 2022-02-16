import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pyjavaproperties import Properties

class BaseTest:

    #driver =None   # Global variable, even if we don't declare python will create it -> as we have decalred 'self.driver' in below method
    #driver --> local variable
    #self.driver --> global variable

    @pytest.fixture(autouse=True)
    def open_close_app(self):

        #Create object of Properties class
        p_file = Properties()
        #open the properties file and load it
        p_file.load(open("config.properties"))

        self.xl_path = p_file['XLPATH']
        #open the browser
        #driver = webdriver.Chrome("./../driver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #maximize the browser
        self.driver.maximize_window()

        #Enter the url
        url= p_file['URL']       #get url from properties file
        self.driver.get(url)

        #Implicit wait
        ito= p_file['ITO']       #get ITO from properties file
        self.driver.implicitly_wait(ito)

        #Explicit wait
        eto = p_file['ETO']  # get ETO from properties file
        self.wait = WebDriverWait(self.driver,eto)
        #self.wait.until(expected_conditions.title_contains("Enter"))


        yield   #Go, run the test and come back

        #close the browser
        self.driver.close()