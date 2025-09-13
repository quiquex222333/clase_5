import pytest

from pages.login_page import LoginPage

def test_login_with_pom(page):
    print("login with pom")
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert page.locator(".inventory_list").is_visible()
    print("fin login with pom")

