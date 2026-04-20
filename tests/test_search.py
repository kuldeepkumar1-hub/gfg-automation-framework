import pytest
from pages.home_page import HomePage
from utils.data_reader import get_test_data
from utils.logger import get_logger

# Initialize logger
logger = get_logger()

# Load test data
data = get_test_data("data/search_data.json")


@pytest.mark.parametrize("search_term", data["search_terms"])
def test_search_functionality(setup, search_term):
    driver = setup

    logger.info(f"Testing search with: {search_term}")

    home_page = HomePage(driver)
    home_page.search(search_term)

    assert search_term.lower() in driver.title.lower()