import time
import unittest

from selenium import webdriver


class MyTests(unittest.TestCase):
    driver = None  # ?

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/kame/Dropbox/software/chromedriver")

    # def test_title_in_google(self):
    #     self.driver.get('https://www.google.com')
    #     time.sleep(3)
    #     self.assertEqual(self.driver.title, 'Google')

    def test_title_in_rms(self):
        self.driver.get('http://89.28.158.00/wPage/Login.aspx')
        time.sleep(3)
        self.assertEqual(self.driver.title, 'Monitoring System')

    # Rotronic ME; Steffen; 10279145

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# web driver chrome

# load page + tab

# find elements
