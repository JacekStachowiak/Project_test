from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class LoginTests():
    
    def test_validLogin(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
    
        sing_log = driver.find_element(By.XPATH, '//div[contains(text(),"Sign Up or Log In")]')
        sing_log.click()
        email = driver.find_element(By.ID, 'email')
        email.clear()
        email.send_keys('test@email.com')
        password = driver.find_element(By.ID, 'password')
        password.clear()
        password.send_keys('abcabc')
        button = driver.find_element(By.XPATH, '//input[@class="btn btn-default btn-block btn-md dynamic-button"]')
        button.click()

        all_course = driver.find_element(By.LINK_TEXT, "ALL COURSES")
        all_course.click()
        search = driver.find_element(By.XPATH, '//input[@id="search"]')
        search.clear()
        search.send_keys('JavaScript')
        button_search = driver.find_element(By.XPATH, '//button[@class="find-course search-course"]')
        button_search.click()
        course = driver.find_element(By.XPATH, '//h4[@class="dynamic-heading"]')
        course.click()
        button_enroll = driver.find_element(By.XPATH, '//button[@class="dynamic-button btn btn-default btn-lg btn-enroll"]')
        button_enroll.click()
       
        driver.quit()

run_test = LoginTests()
run_test.test_validLogin() 

       
            
    

