from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # 🔹 Your custom locator (replace with your XPath if needed)
    search_box = (By.XPATH, "//input[@class='gs-input']")

    def wait_for_page_load(self):
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def search(self, keyword):
        # ✅ Wait for page load
        self.wait_for_page_load()

        # ✅ Wait for search box visible
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        # ✅ Clear + type + ENTER
        search_input.clear()
        search_input.send_keys(keyword + Keys.ENTER)