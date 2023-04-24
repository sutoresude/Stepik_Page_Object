from .pages.main_page import MainPage
import pytest

@pytest.mark.login_guest
class TestLoginFromPage():
    def test1_check_locator_go_to_login(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_locator_go_to_login()

    def test2_check_go_to_login(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_go_to_login()

    def test3_check_login_in_url(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_login_in_url()

    def test4_check_login_form(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_login_form()

    def test5_check_register_form(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_register_form()

    def test_check_full_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.check_all_asserts()

