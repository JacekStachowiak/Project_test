from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.register_page import RegisterPage
from pages.home.navigation_page import NavigationPage
from utilities.readProperties import ReadConfig
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

#@pytest.mark.usefixtures('setUp')
@ddt
class RegisterCSVTest(unittest.TestCase):
    
    baseURL = ReadConfig.getApplicationURL()
    
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-notifications') 
    #options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(baseURL)
       
    @data(*getCSVData('/klon/Project_test/testdata.csv'))
    @unpack
    def test_registerPage(self,fullName, cardnumber, carddata, cardcode, countryname):
        
        self.driver.get(self.baseURL)
        self.rp = RegisterPage(self.driver)
        self.rp.registerCourse(fullName)
        time.sleep(1)
        self.rp.card(cardnumber, carddata, cardcode) 
        time.sleep(1)
        self.rp.country(countryname)
        time.sleep(1)                
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
                        
        self.driver.quit()