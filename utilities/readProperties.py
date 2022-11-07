import configparser
import os

config = configparser.RawConfigParser()
#config = configparser.ConfigParser()

config.read(r'H:\\Klon\\Project_test\\configuration\\config.ini')
#config.read(os.getcwd()+'config.ini')


class ReadConfig():                                  # nawias opcjonalnie teraz nie potrzebny --> dla rozszerzonej tak 
    
    @staticmethod
    def getApplicationURL():
        commonInfo = config["commonInfo"]
        URL = (commonInfo["url"])
        return URL
        
    '''@staticmethod                                   # możemy wywołać bezpośrednio z klasy --> bez tworzenia objektu
    def getApplicationURL():
        URL = config.get('commonInfo', 'url')       # sekcja w config.ini --> nazwa sekcji, pierwszy parametr
        return URL'''
        
    @staticmethod
    def getUseremail():
        username = config.get('commonInfo', 'email')
        return username
    
    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password


