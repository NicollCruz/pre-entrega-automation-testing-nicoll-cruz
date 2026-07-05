import pytest
import os
from datetime import datetime
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

# Hook: Detectar si la prueba falló
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_path = f"reports/screenshots/{test_name}_{timestamp}.png"
            driver_fixture.save_screenshot(screenshot_path)