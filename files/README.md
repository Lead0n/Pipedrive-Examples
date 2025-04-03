# Pipedrive File Downloader & Organizer

## 🚀 Overview
This Python script allows you to **bulk download files from Pipedrive** and automatically **organize them** using a structured naming convention. Instead of manually clicking on each file link, you can run this script to retrieve all your files and store them locally with meaningful names.

### 🔥 Why Use This Script?
✅ **Automated File Retrieval** – No more manual downloads!

✅ **Structured Naming** – Saves files with their **Pipedrive File ID** and related **Deal, Person, Organization, or Lead ID**.  

✅ **Easy Organization** – Quickly locate files by Deal and File ID.

✅ **Seamless Integration** – Works directly with **Pipedrive’s API**.

## 📌 How It Works
The script fetches all files from **Pipedrive's Files API**, identifies their associated **Deal, Person, Organization, or Lead**, and then downloads them using a structured naming pattern:

```plaintext
[file_id]_[deal_id]_[original_filename]
```
For example:
```
00123_0456_contract.pdf  → (File ID 123, related to Deal ID 456)
00987_0321_invoice.png  → (File ID 987, related to Deal ID 321)
```

## 📥 Installation & Setup
### 1️⃣ Prerequisites
- Python 3.8
- Pipedrive API Token
- A few packages: `requests python-dotenv pathvalidate tqdm`
  - (Recommended) You can run thing immediately with [uv](https://github.com/astral-sh/uv) via `uv run`; or
  - Use `pip` instead

### 2️⃣ Setup Instructions
```bash
# Fork this repository and clone it
$ git clone https://github.com/your-repo/pipedrive-file-downloader.git
$ cd pipedrive-file-downloader

# (Optional) If using pip instead of uv, install pip dependencies
$ pip install requests
```

### 3️⃣ Configuration
1. Make a `.env` file and provide API_TOKEN:
```bash
API_TOKEN = YOUR_API_TOKEN
```
with your **Pipedrive API Token**.

2. (Optional) Open the script file (`getAllFiles.py`) change the download folder:
```python
SAVE_PATH = "./pipedrive_files"
```

### 4️⃣ Run the Script
```bash
# using uv
$ uv run getAllFiles.py

# using pip
$ python getAllFiles.py
```

## 📡 About LeadOn
This script is proudly brought to you by **LeadOn**, a powerful tool that connects **WhatsApp Web with Pipedrive** to **centralize your lead management**.

🚀 **What LeadOn Offers:**
- 📩 **Save leads & conversations from WhatsApp Web to Pipedrive**
- 🛠️ **Automate data entry and CRM updates**
- 🔗 **Seamless integration with Pipedrive & WhatsApp Web**

💡 **Join thousands of sales teams who streamline their lead tracking with LeadOn!**

👉 **[Learn more about LeadOn](https://lead-on.co/)**

