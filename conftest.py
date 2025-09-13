import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def five():
    print("Aqui comienza el fixture 5")
    number = 5
    yield number
    number = 0
    print("Aqui termina el fixture 5")


@pytest.fixture
def two():
    return 2


@pytest.fixture(scope="session")
def browser():
    print("Aqui comienza el fixture browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
    print("Aqui termina el fixture browser")



@pytest.fixture()
def page(browser):
    print("Aqui comienza el fixture page")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    print("Aqui termina el fixture page")