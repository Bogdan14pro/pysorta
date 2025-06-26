<p align="center">
  <img src="https://raw.githubusercontent.com/theLroject/py-sorta/main/logo.png" width="220" alt="PySorta logo" />
</p>

# 📁 PySorta: The Pythonic Folder Organizer  ![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Open Source Love](https://img.shields.io/badge/open--source-love-%23ff69b4)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

An open-source Python tool to automatically organize your folders by file type, date modified, or size — built for desktop and iOS (Pythonista). Clean up your Downloads with one command. Contributions welcome!

# 🚿 Lets get cleaning!

Keep your folders tidy and organized with this lightweight Python script that automatically sorts files into subfolders based on:

- ✅ File Type (e.g., Images, Documents, Code, etc.)
- 📅 Date Modified (YYYY-MM folders)
- 📏 File Size (Small / Medium / Large)

Great for Downloads, Desktop folders, or managing cluttered project directories!

---

## 🛠 Features

- Interactive command-line interface
- Organize files by:
  - File type
  - Date modified
  - File size
- Customizable file category mapping
- Works on macOS, Windows, Linux, and even iOS (via [Pythonista](http://omz-software.com/pythonista/))
- Zero dependencies — pure Python!

---

## 🚀 How to Use

### 1. Requirements

- Python 3.x
- Optional: [Pythonista](http://omz-software.com/pythonista/) app for iOS

---

### 2. Run the Script

#### 💻 Mac / Windows / Linux

```bash
python file_organizer_v1.py

Then follow the interactive prompts:
	•	Choose a folder (or leave blank for current)
	•	Select how you’d like to organize: by type, date, or size

⸻

📱 Pythonista on iOS
	1.	Open the script in Pythonista
	2.	Tap ▶️ Play
	3.	Enter a path like . or full iOS-accessible folder path
	4.	Choose your sorting method

✅ Tip: You can hardcode a path in the script if needed (e.g. directory = Path("/private/...")).

⸻

🧩 Customize File Types

Add or edit categories in the FILE_CATEGORIES section of the script:

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "3D Models": [".obj", ".glb", ".fbx"]
}

The script will auto-create folders and move matching files into them.

📂 Example Output

/Downloads
├── Images
│   └── selfie.png
├── Documents
│   └── resume.pdf
├── Code
│   └── tool.py

Or by date:

/Downloads
├── 2024-12
│   └── invoice.pdf
├── 2025-06
│   └── demo.mov

🤝 Contributing

This project is open to the world — whether you’re learning Python or improving tooling for creators.
You’re invited to:
	•	Add new organization modes
	•	Improve cross-platform behavior
	•	Refactor for performance
	•	Build a GUI (Tkinter, web, or iOS-native)
	•	Translate prompts into other languages

Pull requests and feedback are warmly welcomed. 💬

⸻

🪪 License

MIT License
You are free to use, modify, distribute, and build on this project — commercially or privately.

Please keep the original author attribution if redistributing.

⸻

✨ A Note from the Creator

This was built as a small but powerful utility by theProject.  If it helped you, taught you something, or made your life easier — that means everything.
Go build cool things. 🌍.

⸻

💣 A Manifesto for the Imposters

Forget the degrees. We are the Project., the relentless misfits who learned by hacking code apart, learning through trial and error - the hard way, fueled by a burning desire for design, innovation, and access to the deep secrets of the tech frontier. Tragically far too many grest minds lurk on the shadows of feeling like they dont belong - that they are missing some secret that the rest of the community figured out. We are embracing you - and aim to collaborate with any skillset, use proper team work and offer real world support that you can't learn in a book kr a YouTube video.  We don't just create; we defy expectations, building digital marvels that prove our worth with every line of code. We will embrace AI as a tool, not a substitute - and prepare the lost for the new frontier. Welcome to theProject - look forward to working with you.

Hack the planet.
👾 Lithium187
















