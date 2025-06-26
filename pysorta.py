# Welcome to PySorta - v1.0.0 by theProject. We are open to building something cool with anyone of any skill set!
# I have heavily commented the script in an effort to help those learning - feel free to clear them if they get in your way! 

# Import necessary Python modules
import os  # For interacting with the operating system
import shutil  # For moving files
from pathlib import Path  # Modern, cross-platform file paths
from datetime import datetime  # For handling file timestamps

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".cpp", ".c", ".java", ".sh"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Executables": [".exe", ".msi", ".apk", ".dmg", ".pkg"],
    "Others": []  # Catch-all for unknown extensions
}

# Function to determine which category a file extension belongs to
def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"  # Default if no match is found

# Organize files by type/category (e.g., Images, Documents, etc.)
def organize_by_type(directory):
    print("🔤 Organizing by file type...")
    for item in directory.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_folder = directory / category
            dest_folder.mkdir(exist_ok=True)  # Create folder if it doesn't exist
            shutil.move(str(item), dest_folder / item.name)

# Organize files into folders by the month/year they were last modified
def organize_by_date(directory):
    print("📅 Organizing by date modified (YYYY-MM)...")
    for item in directory.iterdir():
        if item.is_file():
            timestamp = item.stat().st_mtime
            date_folder = datetime.fromtimestamp(timestamp).strftime('%Y-%m')
            dest_folder = directory / date_folder
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)

# Organize files by size: Small, Medium, or Large
def organize_by_size(directory):
    print("📏 Organizing by file size...")
    for item in directory.iterdir():
        if item.is_file():
            size = item.stat().st_size  # File size in bytes
            if size < 1 * 1024 * 1024:  # Less than 1MB
                size_folder = "Small (<1MB)"
            elif size < 10 * 1024 * 1024:  # Between 1MB and 10MB
                size_folder = "Medium (1–10MB)"
            else:  # Larger than 10MB
                size_folder = "Large (>10MB)"
            dest_folder = directory / size_folder
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)

# Main function that runs when the script is executed
def main():
    print("📂 Welcome to PySorta - Sorta the Best!")

    # Ask user for the folder to organize (default to current directory)
    path_input = input("📁 Enter folder path (leave blank for current): ").strip() or "."
    directory = Path(path_input).expanduser().resolve()

    if not directory.exists():
        print("❌ Folder not found!")
        return

    # Display sorting options
    print("\nChoose organization mode:")
    print("1. By File Type")
    print("2. By Date Modified")
    print("3. By File Size")

    # Get user's choice
    choice = input("👉 Enter choice [1/2/3]: ").strip()

    # Call the matching function based on user input
    if choice == "1":
        organize_by_type(directory)
    elif choice == "2":
        organize_by_date(directory)
    elif choice == "3":
        organize_by_size(directory)
    else:
        print("❌ Invalid choice. Exiting.")

    print("✅ Done organizing!")

# Entry point — runs the main function only when this file is executed directly
if __name__ == "__main__":
    main()
