import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

username_inputs = ["standard_user"]
# username_inputs = ["standard_user",
#                    "locked_out_user",
#                    "problem_user",
#                    "performance_glitch_user"]
password_inputs = ["secret_sauce"]

first_name = ["Ram",
              "Luxman",
              "Hari",
              "Sita",
              "Geeta"]
last_name = ["Shrestha",
             "Prasad",
             "Gupta",
             "Tiwari",
             "Lama"]
zip_code = ["04662",
            "14738",
            "68023",
            "17563"]
url = "https://www.saucedemo.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()


def user():
    time.sleep(3)
    # UserLogin
    u_name = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    u_name.send_keys(username_inputs)
    pwd = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    pwd.send_keys(password_inputs)
    time.sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]')
    login.click()
    time.sleep(2)
    # Item select
    driver.find_element(By.CSS_SELECTOR, 'select[class="product_sort_container"]').click()
    time.sleep(1)

    select = Select(driver.find_element(By.CSS_SELECTOR, 'select[class="product_sort_container"]'))
    select.select_by_value('lohi')
    time.sleep(2)

    # selected_options = driver.find_element(By.CSS_SELECTOR, '(button[class="btn btn_primary btn_small btn_inventory"])')
    # selected_option = selected_options[1]
    # selected_option.click()

    driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-onesie"]').click()
    time.sleep(2)
    # Checkout
    driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium checkout_button"]').click()
    time.sleep(2)

    f_name = driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
    f_name.send_keys(random.choice(first_name))
    l_name = driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
    l_name.send_keys(random.choice(last_name))
    z_code = driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')
    z_code.send_keys(random.choice(zip_code))
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn btn_primary cart_button btn_action"]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium cart_button"]').click()
    time.sleep(2)

    c_confirmation = driver.find_element(By.CSS_SELECTOR, 'h2[class="complete-header"]')
    check_text = c_confirmation.text

    expected = "THANK YOU FOR YOUR ORDER"
    try:
        assert check_text == expected
        result = "Title Matched"
    except AssertionError:
        result = "Title don't match"
    print(result)

    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn_primary btn_small"]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'a[id="logout_sidebar_link"]').click()
    time.sleep(2)


user()
driver.quit()
