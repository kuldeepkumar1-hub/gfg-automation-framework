from utils.driver_factory import get_driver
from utils.config_reader import load_config

def test_open_website(setup):
    driver = setup

    print("Title:", driver.title)

    assert "GeeksforGeeks" in driver.title