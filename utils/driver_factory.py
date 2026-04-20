from selenium import webdriver
from utils.config_reader import load_config

def get_driver():
    config = load_config()
    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser {browser} not supported")

    driver.maximize_window()
    driver.implicitly_wait(config["timeouts"]["implicit_wait"])

    return driver