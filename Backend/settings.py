import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DEFAULT_USER = os.environ.get("DEFAULT_USERNAME")
DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")
