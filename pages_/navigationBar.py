from selenium.webdriver.common.by import By

class NavigationBar:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_button(self):
        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()