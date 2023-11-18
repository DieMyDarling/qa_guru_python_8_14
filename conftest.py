import os

import pytest
from selene.api import *
from selenium import webdriver

from tools import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.browser_version = '100.0'
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--enable-automation')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')

    selenoid_capability = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }

    login = os.getenv('LOGIN', 'user1')
    password = os.getenv('PASSWORD', '1234')

    options.capabilities.update(selenoid_capability)
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
