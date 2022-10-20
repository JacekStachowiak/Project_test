from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):
    
    @pytest.mark.run(order=1)   
    def test_loginSucces(self): 
         
        baseUrl = 'https://letskodeit.com/'
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
        
        lp.loginSuccesfull('test@email.com', 'abcabc')
        message_succes = lp.loginOk()
        assert message_succes == 'My Account'
        
        self.driver.quit()    
    
    @pytest.mark.run(order=2)
    def test_invalidLogin(self): 
        
        baseUrl = 'https://letskodeit.com/'
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
                        
        lp.loginInValid('test@email.com', 'abcabcABC')
        message_invalid = lp.loginNotOk()
        assert message_invalid == 'Your username or password is invalid. Please try again.'       
        
        driver.quit()
    
    
    