from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CREDENTIAL_FILE_PATH = os.environ.get("CREDENTIAL_FILE_PATH")
