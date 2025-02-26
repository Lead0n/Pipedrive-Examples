# Pipedrive File Downloader & Organizer

## 🚀 Overview
This Python script allows you to **bulk download files from Pipedrive** and automatically **organize them** using a structured naming convention. Instead of manually clicking on each file link, you can run this script to retrieve all your files and store them locally with meaningful names.

### 🔥 Why Use This Script?
✅ **Automated File Retrieval** – No more manual downloads!

✅ **Structured Naming** – Saves files with their **Pipedrive File ID** and related **Deal, Person, Organization, or Lead ID**.  

✅ **Easy Organization** – Quickly locate files by entity type and ID.

✅ **Seamless Integration** – Works directly with **Pipedrive’s API**.

## 📌 How It Works
The script fetches all files from **Pipedrive's Files API**, identifies their associated **Deal, Person, Organization, or Lead**, and then downloads them using a structured naming pattern:

```plaintext
[file_id]_[related_entity_id]_[original_filename]
```
For example:
```
123_456_contract.pdf  → (File ID 123, related to Person ID 456)
987_321_invoice.png  → (File ID 987, related to Deal ID 321)
```

## 📥 Installation & Setup
### 1️⃣ Prerequisites
- Python 3.x
- Pipedrive API Token
- `requests` package (install via `pip install requests`)

### 2️⃣ Setup Instructions
```bash
# Clone this repository
$ git clone https://github.com/your-repo/pipedrive-file-downloader.git
$ cd pipedrive-file-downloader

# Install dependencies
$ pip install requests
```

### 3️⃣ Configuration
1. Open the script file (`download_files.py`) and replace:
```python
API_TOKEN = "YOUR_API_TOKEN"
```
with your **Pipedrive API Token**.

2. (Optional) Change the download folder:
```python
SAVE_PATH = "./pipedrive_files"
```

### 4️⃣ Run the Script
```bash
$ python download_files.py
```

## 📡 About LeadOn
This script is proudly brought to you by **LeadOn**, a powerful tool that connects **WhatsApp Web with Pipedrive** to **centralize your lead management**.

🚀 **What LeadOn Offers:**
- 📩 **Save leads & conversations from WhatsApp Web to Pipedrive**
- 🛠️ **Automate data entry and CRM updates**
- 🔗 **Seamless integration with Pipedrive & WhatsApp Web**

💡 **Join thousands of sales teams who streamline their lead tracking with LeadOn!**

👉 **[Learn more about LeadOn](https://lead-on.co/)**

