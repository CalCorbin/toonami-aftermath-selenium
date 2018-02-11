import unittest
from locators import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

class TestSetUp(object):

    ToonamiURL = ("http://www.toonamiaftermath.com/#")

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def load_page(self):
        driver = self.driver
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_css_selector("div#vid.ustream")
            )

    def check_page_title(self):
        driver = self.driver
        return "Toonami Aftermath | Space is the Place" in driver.title

    def load_video(self):
        driver = self.driver
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_css_selector("#vidembed")
            )

    def click_schedule(self):
        driver = self.driver
        element = self.driver.find_element(*MainPageLocators.SCHEDULE_BUTTON)
        element.click()

class SchedulePage(BasePage):

    scheduleURL = "http://www.toonamiaftermath.com/schedule"

    def load_schedule_page(self):
        driver = self.driver
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_css_selector("div#content.schedule-content")
            )

    def check_schedule_title(self):
        driver = self.driver
        return "Schedule | Space is the Place" in driver.title
