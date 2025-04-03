# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests",
#     "python-dotenv",
#     "pathvalidate",
#     "tqdm",
# ]
# ///
import requests
import os
import json
from tqdm import tqdm
from pathvalidate import sanitize_filename
from dotenv import load_dotenv

# Constants
BASE_URL = "https://api.pipedrive.com/v1/files"
PAGE_LIMIT = 100         # 100 = max files per page per API docs
WIN_PREFIX = "\\\\?\\"   # optional: for long filename support on win10+
SAVE_PATH = "./pipedrive-files"

# Get API_TOKEN from environment variables
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("API_TOKEN is not set in the .env file")

# Create folder if it doesn't exist
os.makedirs(SAVE_PATH, exist_ok=True)

# File list is paginated
page = 0
while True:
    # Get and write page index (don't redo, in case resuming)
    index_path = os.path.join(SAVE_PATH, f"index_{page:04d}_files.json")
    if not os.path.exists(index_path):
        response = requests.get(
            f"{BASE_URL}?api_token={API_TOKEN}&start={page * PAGE_LIMIT}&limit={PAGE_LIMIT}"
        )
        files = response.json().get("data", [])
        with open(index_path, "w", encoding="utf-8") as json_file:
            json.dump(files, json_file, indent=4, ensure_ascii=False)
    else:
        with open(index_path, "r", encoding="utf-8") as json_file:
            files = json.load(json_file)

    # Get and write files
    if files:
        for file in tqdm(files, desc=f"Page {page:04d}", unit="file"):
            if file["remote_location"] != "googledocs":
                file_url = file["url"]
                file_id = file["id"]
                file_deal = file["deal_id"]

                file_name = sanitize_filename(file["name"])
                file_name = f"{file_id:05d}_{file_deal or 0:04d}_{file_name}"
                file_path = (
                    f"{WIN_PREFIX}{os.path.abspath(os.path.join(SAVE_PATH, file_name))}"
                )

                if not os.path.exists(file_path):
                    file_response = requests.get(f"{file_url}?api_token={API_TOKEN}")
                    if file_response.status_code == 200:
                        with open(file_path, "wb") as f:
                            f.write(file_response.content)
                    else:
                        print(
                            f"\nError downloading {file_name} [Code {file_response.status_code}]"
                        )
    else:
        print("No files found.")
        break

    page += 1
