# logger.py

import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Set up the logger
logger = logging.getLogger("AntivirusLogger")
logger.setLevel(logging.DEBUG)

# File handler for logging
file_handler = logging.FileHandler("logs/antivirus.log")
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage (you can import and use this logger from other files)
if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
