from selenium.webdriver.common.by import By
class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    #getting username and assigning username
    def enter_username(self, username):
        username_input = self.driver.find_element(By.XPATH, "//input[@id='username']")
        username_input.send_keys(username)

    #getting password and assigning password
    def enter_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys(password)

    #getting login button and clicking the button
    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//input[@name='signin']")
        login_button.click()

    #fetching the text to see successful login
    def text_fetch(self):
        return self.driver.find_element(By.LINK_TEXT, "ProtoCommerce Home").text
