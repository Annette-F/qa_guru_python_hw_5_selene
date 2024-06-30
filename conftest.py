import pytest

from selene import browser

@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1024
    browser.config.window_height = 1280

    yield

    browser.quit()




