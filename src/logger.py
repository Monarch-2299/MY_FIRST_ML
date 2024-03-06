import logging
import os
from datetime import datetime

# Create a filename for the log file using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory named "logs" in the current working directory if it doesn't exist already
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Construct the full path to the log file inside the "logs" directory
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Log a message indicating that logging has started if the script is run directly
if __name__ == "__main__":
    logging.info("Logging has started")
