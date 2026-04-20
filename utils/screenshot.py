import os
from datetime import datetime

def take_screenshot(driver, name):
    os.makedirs("reports/screenshots", exist_ok=True)

    # ✅ Clean filename (remove spaces & special chars)
    name = name.replace(" ", "_").replace("[", "").replace("]", "")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"reports/screenshots/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)
    return file_path