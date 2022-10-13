from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage():
    
    # locators
    _sing_log = '//div[contains(text(),"Sign Up or Log In")]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _verify_login = '//span[@class="dynamic-text help-block"]'
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        sing_log = self.driver.find_element(By.XPATH, self._sing_log)
        sing_log.click()
        emailField = self.driver.find_element(By.ID, self._email_field)
        emailField.clear()
        emailField.send_keys(username) 
        passwordField = self.driver.find_element(By.ID, self._password_field)
        passwordField.clear()
        passwordField.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH, self._login_button)
        loginButton.click() 

