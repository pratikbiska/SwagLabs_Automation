from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Asrt:
    def __init__(self, driver):
        self.driver = driver
        self.assertion_context = (By.CSS_SELECTOR, 'h2[class="complete-header"]')

    def check_assertion(self, expected):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.assertion_context)
        )
        check_text = (self.driver.find_element(*self.assertion_context)).text
        try:
            assert check_text == expected
            result = "Order Confirmation received."
        except AssertionError:
            result = "Order Confirmation not received."
        print(result)

