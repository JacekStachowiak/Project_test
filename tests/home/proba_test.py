from pages.home.register_page2 import RegisterPage
import unittest
from selenium import webdriver
import pytest
import time
from utilities.readProperties import ReadConfig
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


baseURL = ReadConfig.getApplicationURL()
    
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications') 
#options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseURL)
    
data = [('JavaScript for beginners','1234 2345 3456 4567','10/24','345','Poland'),
        ('Complete Test Automation Bundle', '1234 2345 3456 4567', '10/24', '345', 'Poland'),
        ('Rest API Automation With Rest Assured', '1234 2345 3456 4567', '10/25', '465', 'Canada')] 
                     
@pytest.mark.run(order=1)
@pytest.mark.parametrize('fullName, cardnumber, carddata, cardcode, countryname', data)
def test_register_page2(fullName, cardnumber, carddata, cardcode, countryname):
        
    rp = RegisterPage(driver)       
    rp.registerCourse(fullName)
    time.sleep(1)
    rp.card(cardnumber, carddata, cardcode) 
    time.sleep(1)
    rp.country(countryname)
    time.sleep(1)
               
    message = rp.errorCardNumber()
    assert message == 'Numer karty jest nieprawidłowy.' 
        
    #self.driver.close()