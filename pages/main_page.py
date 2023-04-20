from .login_page import LoginPage
from .locators import MainPageLocators
class MainPage(LoginPage):

    def check_all_asserts(self):
        self.should_be_login_link()
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

