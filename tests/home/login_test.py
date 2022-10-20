from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest
import pytest

class LoginTest(unittest.TestCase):
    
    @pytest.mark.run(order=2)
    def test_invalidLogin(self): 
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        lp = LoginPage(driver)       
        driver.get(baseUrl)
        
        lp.loginInValid('test@email.com', 'abcabcABC')
        message_invalid = lp.loginNotOk()
        assert message_invalid == 'Your username or password is invalid. Please try again.'       
        driver.quit()
    
                 
    @pytest.mark.run(order=1)   # kolejność testów
    def test_loginSucces(self):  
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        lp = LoginPage(driver) 
        driver.get(baseUrl)
        
        lp.loginSuccesfull('test@email.com', 'abcabc')
        lp.logout()
        message_succes = lp.loginOk()
        assert message_succes == 'My Account'
   
        driver.quit()
           
                
        

