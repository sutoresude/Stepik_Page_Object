from .login_page import LoginPage
from .locators import MainPageLocators
from .product_page import ProductPage
from .locators import ProductPageLocators

class MainPage(LoginPage):

    def check_locator_go_to_login(self):
        self.should_be_login_link()

    def check_go_to_login(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()

    def check_login_in_url(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_url()

    def check_login_form(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_form()

    def check_register_form(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_register_form()

    def check_all_asserts(self):
        self.should_be_login_link()
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

class MainPage2(ProductPage):

    def check_basket(self):
        self.should_be_basket()
        link_smoke = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link_smoke.click()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()



