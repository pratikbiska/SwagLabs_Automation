from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FIN:
    def __init__(self, driver):
        self.driver = driver
        self.complete = (By.CSS_SELECTOR, 'button[class="btn btn_primary btn_small"]')

    def click_back_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.complete)
        )
        self.driver.find_element(*self.complete).click()
