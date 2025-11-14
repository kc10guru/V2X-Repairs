import pandas as pd
from pathlib import Path
import os

# Path to the Excel file in Downloads
downloads_path = Path.home() / "Downloads"
file_path = downloads_path / "E6 Engineering request.xlsx"

print(f"Looking for file: {file_path}")

if not file_path.exists():
    print(f"Error: File not found at {file_path}")
    print("Please make sure the file name is correct and it's in your Downloads folder.")
    exit()

print("Reading Excel file...")

# Read the Excel file
df = pd.read_excel(file_path)

print(f"File loaded successfully! Total rows: {len(df)}")
print(f"\nColumn names: {list(df.columns)}")

# Get column E (index 4, since it's 0-based)
# The header row is automatically detected by pandas
part_number_column = df.iloc[:, 4]  # Column E (5th column)
print(f"\nColumn E header: {df.columns[4]}")

# Find duplicates in column E
# Create a mask for all rows where the part number appears more than once
duplicate_mask = df.iloc[:, 4].duplicated(keep=False)

# Get all rows with duplicate part numbers
duplicates_df = df[duplicate_mask]

print(f"\nFound {len(duplicates_df)} rows with duplicate part numbers")
print(f"Number of unique duplicate part numbers: {duplicates_df.iloc[:, 4].nunique()}")

if len(duplicates_df) > 0:
    print("\nDuplicate part numbers found:")
    duplicate_parts = duplicates_df.iloc[:, 4].value_counts()
    for part, count in duplicate_parts.items():
        print(f"  {part}: appears {count} times")
    
    # Load the Excel file with openpyxl to add a new sheet
    print("\nCreating new sheet with duplicates...")
    
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # Write duplicates to a new sheet
        duplicates_df.to_excel(writer, sheet_name='Duplicates', index=False)
    
    print(f"\n✓ Success! Duplicates have been extracted to a new sheet called 'Duplicates'")
    print(f"✓ File saved: {file_path}")
    
else:
    print("\nNo duplicate part numbers found!")

print("\nPress Enter to close...")
input()

