from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def delete_first_product_from_cart(self):
        cart_icon_element = self.driver.find_element(By.ID, 'nav-cart')
        cart_icon_element.click()

        delete_button_locator = (By.XPATH, "(//input[contains(@value, 'Delete')])[1]")
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(delete_button_locator)
        )
        delete_button.click()

    def view_cart(self):
        pass