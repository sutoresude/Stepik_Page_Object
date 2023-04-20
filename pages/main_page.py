from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
class MainPage(BasePage):
    def go_to_login_page(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"