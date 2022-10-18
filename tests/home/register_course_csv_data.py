from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.register_page import RegisterPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@ddt
class RegisterCSVTest(unittest.TestCase):
    
    baseUrl = 'https://courses.letskodeit.com/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    rp = RegisterPage(driver)
    
    @data(*getCSVData('/klon/Project_test/testdata.csv'))
    @unpack
    def test_registerPage(self, namecourse, cardnumber, carddata, cardcode, countryname):
        
        self.rp.registerCourse(namecourse)
        self.rp.card(cardnumber, carddata, cardcode) 
        self.rp.country(countryname)
                
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
                
        self.driver.quit()