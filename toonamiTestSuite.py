import unittest
from page import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ToonamiAftemathOnlineTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestSetUp.ToonamiURL)
        self.driver.maximize_window()

    def test_verify_site_is_online(self):
        main_page = MainPage(self.driver)
        main_page.load_page()
        assert main_page.check_page_title(), "The main title isn't there."
        self.driver.get(SchedulePage.scheduleURL)
        schedule_page = SchedulePage(self.driver)
        schedule_page.load_schedule_page()
        assert schedule_page.check_schedule_title(), "The schedule title isn't there."

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
