from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os,sys
sys.path.append(os.getcwd())
from config.variable import *

class Common():

    def __init__(self):
        self.driver = driver

    def _open_url(self,url=browser_url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

    def _do_click(self,type,element,timeout=30):
        obj = self._selenium_methods(type, element,timeout)
        obj.click()

    def _do_sendkeys(self,type,element,input,timeout=30):
        obj=self._selenium_methods(type, element,timeout)
        obj.send_keys(input)

    def _close_browser(self):
        self.driver.close()

    def _do_move_to_element_click(self,type,element,timeout=30):
        obj = self._selenium_methods(type, element, timeout)
        ActionChains(self.driver).move_to_element(obj).click().perform()

    def _selenium_methods(self,type,element,timeout):
        if type.lower() == 'id':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.ID, element)))
            obj = self.driver.find_element_by_id(element)
        elif type.lower() == 'xpath':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, element)))
            obj = self.driver.find_element_by_xpath(element)
        elif type.lower() == 'name':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.NAME, element)))
            obj = self.driver.find_element_by_name(element)
        elif type.lower() == 'css':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element)))
            obj = self.driver.find_element_by_css_selector(element)
        elif type.lower() == 'class':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME, element)))
            obj = self.driver.find_element_by_class_name(element)
        return obj

if __name__ == '__main__':
    pass







