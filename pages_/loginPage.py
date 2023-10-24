from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_username(self, username):
        email_input = self.driver.find_element(By.ID, "ap_email")
        email_input.send_keys(username)

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def fill_password(self, password):
        password_input = self.driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password)

    def click_signin(self):
        signin_button = self.driver.find_element(By.ID, "signInSubmit")
        signin_button.click()