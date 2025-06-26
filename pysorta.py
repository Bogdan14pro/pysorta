# Welcome to PySorta v1.0.0 – by theProject.
# We’re building something cool with anyone of any skill level.
# This script is heavily commented to help beginners — feel free to remove comments if needed.

import shutil  # For moving files between folders
from pathlib import Path  # For safe, cross-platform path handling
from datetime import datetime  # For organizing by last modified time

# 🎯 Define file categories and associated extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"
    ],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Code": [
        ".py", ".js", ".ts", ".html", ".css", ".cpp", ".c", ".java", ".sh"
    ],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Executables": [".exe", ".msi", ".apk", ".dmg", ".pkg"],
    "Others": []  # Everything else
}


def get_category(extension):
    """Return the file category based on extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_by_type(directory):
    """Organize files into folders based on file type."""
    print("🔤 Organizing by file type...")
    for item in directory.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_folder = directory / category
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)


def organize_by_date(directory):
    """Organize files into folders based on last modified date."""
    print("📅 Organizing by date modified (YYYY-MM)...")
    for item in directory.iterdir():
        if item.is_file():
            timestamp = item.stat().st_mtime
            folder_name = datetime.fromtimestamp(timestamp).strftime('%Y-%m')
            dest_folder = directory / folder_name
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)


def organize_by_size(directory):
    """Organize files into folders based on file size."""
    print("📏 Organizing by file size...")
    for item in directory.iterdir():
        if item.is_file():
            size = item.stat().st_size  # Size in bytes
            if size < 1 * 1024 * 1024:
                size_folder = "Small (<1MB)"
            elif size < 10 * 1024 * 1024:
                size_folder = "Medium (1–10MB)"
            else:
                size_folder = "Large (>10MB)"
            dest_folder = directory / size_folder
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)


def main():
    """Main entry point for PySorta."""
    print("📂 Welcome to PySorta – Sorta the Best!")

    path_input = input(
        "📁 Enter folder path (leave blank for current): "
    ).strip() or "."

    directory = Path(path_input).expanduser().resolve()

    if not directory.exists():
        print("❌ Folder not found!")
        return

    print("\nChoose organization mode:")
    print("1. By File Type")
    print("2. By Date Modified")
    print("3. By File Size")

    choice = input("👉 Enter choice [1/2/3]: ").strip()

    if choice == "1":
        organize_by_type(directory)
    elif choice == "2":
        organize_by_date(directory)
    elif choice == "3":
        organize_by_size(directory)
    else:
        print("❌ Invalid choice. Exiting.")
        return

    print("✅ Done organizing!")


if __name__ == "__main__":
    main()
