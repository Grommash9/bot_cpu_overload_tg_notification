import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
import os

cwd = Path().cwd()


TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CPU_USAGE = int(os.getenv('CPU_USAGE'))
RAM_USAGE = int(os.getenv('RAM_USAGE'))
DISK_FREE_SPACE = int(os.getenv('DISK_FREE_SPACE'))
SERVER_NAME = os.getenv('SERVER_NAME')

