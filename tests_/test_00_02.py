import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.cartPage import CartPage
from pages_.loginPage import  LoginPage
from pages_.navigationBar import  NavigationBar


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com"
           "%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
           "%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F"
           "%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPage = LoginPage(driver)
loginPage.fill_username("sona.ghukasyan@gmail.com")
time.sleep(2)
loginPage.click_continue()
loginPage.fill_password("hasiko07")
loginPage.click_signin()


navigationBar = NavigationBar(driver)
navigationBar.click_cart_button()

cartPage = CartPage(driver)
cartPage.view_cart()
cartPage.view_cart()

first_product_delete_button_element = driver.find_element(By.XPATH, "(//input[@value='Delete'])[1]")
first_product_delete_button_element.click()

time.sleep(5)

driver.close()

