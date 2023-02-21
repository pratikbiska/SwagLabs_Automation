from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Test1.Pages.Login import UserLogin
from Test1.Pages.Products import Product
from Test1.Pages.YourCart import Cart
from Test1.Pages.YourInfo import Info
from Test1.Pages.Overview import OView
from Test1.Pages.Complete import FIN
from Test1.Pages.HBurger import Burger
from Test1.Pages.Assertion import Asrt

import random
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
login_page = UserLogin(driver)
product_page = Product(driver)
cart_page = Cart(driver)
info_page = Info(driver)
overview_page = OView(driver)
complete_page = FIN(driver)
hamburger_menu = Burger(driver)
assertion_check = Asrt(driver)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username_inputs = ["standard_user"]
password_inputs = ["secret_sauce"]
sort_by = ["az",'za',"lohi","hilo"]
first_n = ["Ram",
            "Luxman",
            "Hari",
            "Sita",
            "Geeta"]
last_n = ["Shrestha",
          "Prasad",
          "Gupta",
          "Tiwari",
          "Lama"]
zip_c = ["04662",
         "14738",
         "68023",
         "17563"]
expected = "THANK YOU FOR YOUR ORDER"

# login
login_page.set_username(username_inputs)
login_page.set_password(password_inputs)
time.sleep(2)
login_page.click_login()

# Product
time.sleep(2)
product_page.click_filter()
product_page.select_filter(sort_by[2])
time.sleep(2)
product_page.select_product()
time.sleep(2)

# Checkout
cart_page.click_cart()
time.sleep(2)
cart_page.click_checkout()
time.sleep(2)

# Checkout: Your Information
info_page.first_name(random.choice(first_n))
info_page.last_name(random.choice(last_n))
info_page.zip_code(random.choice(zip_c))
time.sleep(2)
info_page.click_continue()
time.sleep(2)

# Checkout: Overview
overview_page.click_finish()
time.sleep(2)

# Assertion
assertion_check.check_assertion(expected)
time.sleep(2)

# Checkout: COMPLETE!
complete_page.click_back_home()
time.sleep(2)

# Hamburger Menu
hamburger_menu.click_menu()
time.sleep(2)
hamburger_menu.click_logout()
time.sleep(10)

driver.quit()








