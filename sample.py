# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.guru99.com/software-testing-seven-principles.html")
        driver.find_element_by_xpath("//section[@id='g-container-main']/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[4]/div/div/div/div[2]/div").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("12345678")
        driver.find_element_by_xpath("//div[@id='passwordNext']/div/button/div[2]").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//div[@id='passwordNext']/div/button/div[2]").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("oorer0531")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[@id=':cc']/div/div").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()