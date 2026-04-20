from loguru import logger
import os

# Create logs folder if not exists
os.makedirs("reports/logs", exist_ok=True)

logger.add("reports/logs/test.log", rotation="1 MB", level="INFO")

def get_logger():
    return logger