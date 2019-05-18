import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.DealsPage import DealsPage
from Pages.ProductPage import ProductPage


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "/Users/User/Documents/CACC/Module 5 - Automation/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_eBay(self):
        driver = self.driver
        driver.get("https://www.ebay.ca")

        homepage = HomePage(driver)
        homepage.click_signin()

        login = LoginPage(driver)
        login.enter_username("maya.bogatskaya@gmail.com")
        login.enter_password("MayaeBay123456!")
        login.click_signin()

        homepage = HomePage(driver)
        homepage.click_deals()

        dealspage = DealsPage(driver)
        dealspage.click_product()

        productpage = ProductPage(driver)
        productpage.click_addtocart()

        homepage = HomePage(driver)
        homepage.signout()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/User/PycharmProjects/Sel_Practice/venv/Lib/site-packages/HtmlTestRunner"),verbosity=2)


