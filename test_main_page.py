from .pages.login_page import LoginPage
from .pages.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"

def test_chek_full_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.check_all_asserts()

