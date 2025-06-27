"""
PySorta v1.0.0 by theProject.

This script organizes files in a directory by type, size, or modification date.
It’s heavily commented for beginners. Contributions welcome!
"""

import shutil
from pathlib import Path
from datetime import datetime

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
    "Others": []
}


def get_category(extension):
    """
    Return the file category based on its extension.

    Args:
        extension (str): The file extension (e.g., '.jpg', '.pdf').

    Returns:
        str: The category name corresponding to the extension, or 'Others' if no match is found.
    """

    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_by_type(directory):
    """
    Organize files in the given directory into subfolders based on file type.

    Args:
        directory (Path): A pathlib.Path object representing the directory to organize.

    Side Effects:
        Moves files into folders named after their categories (e.g., 'Images', 'Documents').
    """

    print("🔤 Organizing by file type...")
    for item in directory.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_folder = directory / category
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)


def organize_by_date(directory):
    """
    Organize files in the given directory into subfolders by last modified date (YYYY-MM format).

    Args:
        directory (Path): A pathlib.Path object representing the directory to organize.

    Side Effects:
        Moves files into folders named by year and month (e.g., '2024-06').
    """

    print("📅 Organizing by date modified (YYYY-MM)...")
    for item in directory.iterdir():
        if item.is_file():
            timestamp = item.stat().st_mtime
            folder_name = datetime.fromtimestamp(timestamp).strftime('%Y-%m')
            dest_folder = directory / folder_name
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)


def organize_by_size(directory):
    """
    Organize files in the given directory into subfolders based on file size.

    Size categories:
        - Small (<1MB)
        - Medium (1–10MB)
        - Large (>10MB)

    Args:
        directory (Path): A pathlib.Path object representing the directory to organize.

    Side Effects:
        Moves files into folders named after size categories.
    """

    print("📏 Organizing by file size...")
    for item in directory.iterdir():
        if item.is_file():
            size = item.stat().st_size
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
    """
    Main entry point for PySorta.

    Prompts the user to input a folder path (defaults to current directory if blank),
    then allows them to choose how to organize the files in that folder:
        1. By File Type
        2. By Date Modified
        3. By File Size

    Based on the selected option, the appropriate organization function is called.
    Files in the specified directory will be moved into categorized subfolders.

    Side Effects:
        Prints messages to the console and moves files on the file system.
    """

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
