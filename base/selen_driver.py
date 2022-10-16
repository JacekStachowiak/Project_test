import logging
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import * 
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl

class SelenDriver():
    
    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        self.driver = driver
    
    def getByType(self, locatorType):        # def dla By.ID i By.Xpath
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'text':
            return By.LINK_TEXT
        else:
            print(f'Ten typ locatora {locatorType} nie jest wspierany/nie jest dobry')
        return False            


    def getElement(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator) 
            print(f'Element found with locator: {locator}, and locatorType: {locatorType}')           
        except:
            print(f'Element not found with locator: {locator}, and locatorType: {locatorType}')
        return element            


    def getElementList(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator) 
            print(f'Element list found with locator: {locator}, and locatorType: {locatorType}')           
        except:
            print(f'Element list not found with locator: {locator}, and locatorType: {locatorType}')
        return element
  
    
    def startFrame(self, locator, locatorType = 'id'):
        try:
            frame = self.getElement(locator, locatorType)
            element = self.driver.switch_to.frame(frame)
            print('Start Frame - found')
        except:
            print('Start Frame not found')  
        return element   
  
    
    def endFrame(self):
        element = self.driver.switch_to.default_content()
        return element 


    def select(self, countryname, locator, locatorType='id'):
        element = self.getElement(locator, locatorType)
        element2 = Select(element)
        element2.select_by_visible_text(countryname)
   
    
    def elementClick(self, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            print(f'Cliked on the element with locator: {locator}, locatorType: {locatorType}')
        except:
            print(f'Cannot clik on the element with locator: {locator}, locatorType: {locatorType}')
            print_stack()
    
    
    def sendKeys(self, data, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(f'Send data on  element with locator: {locator}, locatorType: {locatorType}')
        except:
            print(f'Cannot send data on the element with locator: {locator}, locatorType: {locatorType}')
            print_stack()
    
    
    def getText(self, locator='', locatorType='id', element=None, info=''):
        try:
            if locator:
                print('In locator condition')
                element = self.getElement(locator, locatorType)
            print('Before finding text')
            text = element.text
            long = str(len(text))
            if long == 0:
                text = element.get_attribute('innerText')
            if long != 0:
                print(f'Getting text on element :: {info}')
                print(f'The text is :: {text}')
                text = text.strip()
        except:
            print(f'Failed to get text on element {info}')
            print_stack()
            text = None
        return text            
    
    def errorCard(self, locator='', locatorType='id'):
        
        element = self.getElement(locator, locatorType)
        message = element.text
        if message is not None:
            print(f'Element znaleziony: {message}')
        else:
            print('Wszystko w porządku') 
        return message            

    # aby sprawdzić czy element jest obecny na stronie - czy będzie false czy True cały czas testujemy (nie wyrzuci)
    def isElementPresent(self, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType) # By.Id, 'name'
            if element is not None:
                print(f'Element present with locator: {locator}, locatorType: {locatorType}')
                return True
            else: 
                print(f'Element not present with locator: {locator}, locatorType: {locatorType}')
                return False
        except:
            print('Element not found')
            return False
    
    def isElementDisplayed(self, locator='', locatorType='id', element=None):
        
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                print(f'Element is displayed with locator: {locator}, locatorType: {locatorType}')                
            else:
                print(f'Element is not displayed with locator: {locator}, locatorType: {locatorType}')                
            return isDisplayed
        except:
            print('Element not found')
            return False

    
    # drugi sposób na obecność elementu
    def elementPresentCheck(self, byType, locator):
        try:
            elementList = self.driver.find_elements(byType, locator) # By.Id, 'name'
            if len(elementList) > 0:
                print(f'Element present with locator: {locator}, locatorType: {str(byType)}')
                return True
            else:
                print(f'Element not present with locator: {locator}, locatorType: {str(byType)}')
                return False
        except:
            print('Element not found')
            return False


    def waitForElement(self, locator, locatorType = 'id',timeout_1=10, pollFrequency_1=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print(f'Waiting for maximum:: {timeout_1} :: second for element to be visible')
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=pollFrequency_1, ignored_exceptions=[
                                                                                        NoSuchElementException,
                                                                                        ElementNotVisibleException,
                                                                                        ElementNotSelectableException ]) 
            element = wait.until(EC.visibility_of_element_located((byType, locator))) # uwaga na ilośc nawiasów
            print('Element appeared (pojawił się) on the web page')
        except:
            print('Element not appeared on the page')
            print_stack()  # ślad stosu
        return element         

    
    def webScroll(self, direction='up'):
        
        if direction == 'up':
            self.driver.execute_script('window.scrollBy(0, -1000);')
        
        if direction == 'down':
            self.driver.execute_script('window.scrollBy(0, 700);')            
        
          
        
        