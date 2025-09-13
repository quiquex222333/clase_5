from pages.base_page import BasePage

class LoginPageDry(BasePage):
    user = "input[data-test='username']"
    pwd  = "input[data-test='password']"
    btn  = "input[data-test='login-button']"

    def open(self): self.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.fill(self.user, username)
        self.fill(self.pwd, password)
        self.click(self.btn)
