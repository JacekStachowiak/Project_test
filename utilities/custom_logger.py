
import logging
import inspect

def customLogger(loglevel=logging.DEBUG):
    
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By defaul log all messages
    logger.setLevel(logging.DEBUG)
    
    fileHandler = logging.FileHandler('automation.log', mode='w')
    fileHandler.setLevel(loglevel)
    
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M %p')
    
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    
    return logger