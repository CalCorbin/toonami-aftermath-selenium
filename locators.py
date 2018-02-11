from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SCHEDULE_BUTTON = (By.CSS_SELECTOR, "a:nth-child(2)")
    PAGE_TITLE = (By.XPATH, "//*[@id='page']/footer/text()")
