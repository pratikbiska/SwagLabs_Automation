from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Burger:
    def __init__(self, driver):
        self.driver = driver
        self.menu = (By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
        self.logout = (By.CSS_SELECTOR, 'a[id="logout_sidebar_link"]')

    def click_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu)
        )
        self.driver.find_element(*self.menu).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout)
        )
        self.driver.find_element(*self.logout).click()