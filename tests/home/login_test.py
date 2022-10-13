from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest
class LoginTest(unittest.TestCase):
    
    def test_validLogin(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
        lp.login('test@email.com', 'abcabcABC')

        verifyLogin = driver.find_element(By.XPATH, '//span[@class="dynamic-text help-block"]').text
        
        if verifyLogin is not None:
            print(f'Element znaleziony: {verifyLogin}')
            assert verifyLogin == 'Your username or password is invalid. Please try again.'
        else:
            print('Nie ma elementu')            

        driver.quit()

