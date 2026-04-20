import pytest
from utils.driver_factory import get_driver
from utils.config_reader import load_config
from utils.screenshot import take_screenshot
from utils.logger import get_logger

logger = get_logger()


@pytest.fixture
def setup(request):
    config = load_config()
    driver = get_driver()
    driver.get(config["base_url"])

    yield driver

    # 👇 Access test result correctly
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = take_screenshot(driver, test_name)
        logger.error(f"Test Failed: {test_name}, Screenshot: {screenshot_path}")

    driver.quit()


# 👇 VERY IMPORTANT HOOK (must be correct)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)