'''
func:use logging module, print output info to file and console.
author:Lele Wu.
time:2020/8/8
'''
import logging

def getLogger(logPath):
    logger = logging.getLogger('info')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] %(message)s')

    std_handler = logging.StreamHandler()
    std_handler.setLevel(logger.level)
    std_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(logPath)
    file_handler.setLevel(logger.level)
    file_handler.setFormatter(formatter)

    logger.addHandler(std_handler)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger = getLogger('./log/output.log')
    logger.info('i can print info to console and file in real time | use logger.info replace print')