from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

class LoginTests():
    
    def test_error(self):
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

        driver.execute_script("window.scrollBy(0,700);")    # poziom i drugi: zakres dokąd
        time.sleep(3)
        
        driver.switch_to.frame(0)
        card_number = driver.find_element(By.XPATH, '//div[@id="root"]/form//div[@class="CardNumberField CardNumberField--ltr"]//input[@name="cardnumber"]')        
        card_number.clear()
        card_number.send_keys('1234 2345 3456 4567')
        time.sleep(4)
        
        error = driver.find_element(By.XPATH, '//div[@class="card-errors has-error"]')
        assert error == 'Numer karty jest nieprawidłowy.'
        
        
        '''
        card_data = driver.find_element(By.XPATH, '//input[@name="exp-date"]')
        card_data.clear()
        card_data.send_keys('10/23')
        
        card_code = driver.find_element(By.XPATH, '//input[@name="cvc"]')
        card_code.clear()
        card_code.send_keys('345')
        
        country = driver.find_element(By.NAME, 'country-list')
        card_country = Select(country)
        card_country.select_by_visible_text('Poland')
        '''
        driver.quit()

run_test = LoginTests()
run_test.test_error() 

       
            
    

