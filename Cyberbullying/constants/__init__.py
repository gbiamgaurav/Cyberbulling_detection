import os

from datetime import datetime



# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'cyberbullying_detection'
ZIP_FILE_NAME = 'youtube_parsed_dataset.csv.zip'
LABEL = 'label'
TEXT = 'text'
MODEL_NAME = 'model.h5'
APP_HOST = "0.0.0.0"
APP_PORT = 8080

