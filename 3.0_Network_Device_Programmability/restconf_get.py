
import os
from dotenv import load_dotenv
from pathlib import Path
import requests


# Get the directory this script is in
script_dir = Path(__file__).resolve().parent

dotenv_path = script_dir / "config" / ".env"
load_dotenv(dotenv_path=dotenv_path)

port = os.getenv("DCLOUD_PORT")

print(f"the port is {port}")


