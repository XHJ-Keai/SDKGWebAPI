import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
DATA_DIR = str(Path(ROOT_DIR) / "data")  # This is the data of this project
OUTPUT_DIR = str(Path(ROOT_DIR) / "output")
