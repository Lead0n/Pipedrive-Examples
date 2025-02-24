import requests
import os

API_TOKEN = "YOUR_API_TOKEN"
BASE_URL = "https://api.pipedrive.com/v1/files"
SAVE_PATH = "./pipedrive_files"

# Create folder if it doesn't exist
os.makedirs(SAVE_PATH, exist_ok=True)

# Get list of files
response = requests.get(f"{BASE_URL}?api_token={API_TOKEN}")
files = response.json().get("data", [])

if files:
    for file in files:
        file_name = file["name"]
        file_url = file["url"]
        
        # Download the file
        file_response = requests.get(file_url)
        if file_response.status_code == 200:
            with open(os.path.join(SAVE_PATH, file_name), "wb") as f:
                f.write(file_response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Error downloading {file_name}")
else:
    print("No files found.")
