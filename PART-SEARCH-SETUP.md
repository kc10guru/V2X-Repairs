# Part Number Search Setup Instructions

## Overview
Your index page now searches for part numbers from your Excel spreadsheet and displays a message asking customers to contact your sales team.

## Setup Steps

### Step 1: Convert Excel to JSON

1. **Open the converter tool:**
   - Open `convert-excel-to-json.html` in your web browser

2. **Prepare your Excel file:**
   - Open `IW39 3OCT2025 for Jeff.xlsx` in Excel
   - Click **File → Save As**
   - Choose **CSV (Comma delimited) (*.csv)** format
   - Save it as `parts-database.csv` (or any name you like)

3. **Convert to JSON:**
   - In the converter tool, upload your CSV file
   - Click "Convert to JSON"
   - Review the preview to ensure it looks correct
   - Click "Download parts-database.json"
   - Save the downloaded file to your **V2X-Repairs** folder

### Step 2: Test the Search

1. Open `index.html` in your web browser
2. Enter a part number from your spreadsheet
3. Click "Search"
4. You should see:
   - **If found:** Green success message with part number, description, and contact email
   - **If not found:** Red error message asking to verify the part number

## How It Works

- The `parts-database.json` file contains all your part numbers and descriptions
- When someone searches, it looks up the part number (case-insensitive)
- If found, it displays the part info and directs them to email **repairs@gov2x.com**
- If not found, it shows an error and still provides the contact email

## Updating the Parts Database

Whenever you update your Excel spreadsheet:

1. Export it to CSV again
2. Use the converter tool to generate a new `parts-database.json`
3. Replace the old JSON file in your V2X-Repairs folder
4. Refresh your website - the new parts will be available immediately

## Expected Format

Your Excel/CSV should have these columns:
- **Material**: The part number (e.g., "WS-1001", "LG-2001")
- **Material Description**: The part name/description

The converter will automatically find these columns even if they're not the first columns.

## Troubleshooting

**"Parts database is still loading"**
- Wait a moment and try again
- Check that `parts-database.json` exists in the same folder as `index.html`

**"Part number not found"**
- Verify the part number is in your Excel file
- Check for extra spaces or different formatting
- The search is case-insensitive, so "WS-1001" and "ws-1001" are treated the same

**"Error loading parts database"**
- Make sure `parts-database.json` exists in the V2X-Repairs folder
- If testing locally, you may need to run a local web server (browsers block file:// protocol JSON loading)
- To run a simple server: Open PowerShell in your V2X-Repairs folder and run:
  ```
  python -m http.server 8000
  ```
  Then visit `http://localhost:8000` in your browser

## Files

- `index.html` - Main page with search functionality (updated)
- `convert-excel-to-json.html` - Tool to convert your Excel/CSV to JSON
- `parts-database.json` - Your parts lookup database (you need to create this)
- `IW39 3OCT2025 for Jeff.xlsx` - Your original Excel file

