<p align="center">
  <img src="https://raw.githubusercontent.com/theProject/pysorta/main/logo.png" width="220" alt="PySorta logo" />
</p>

# <p align="center">🗂️ PySorta: The Pythonic Folder Organizer</p>

<div align="center">
	
![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Open Source Love](https://img.shields.io/badge/open--source-love-%23ff69b4)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

</div>

***

❔ PySorta is an open-source Python tool to automatically organize your folders by file type, date modified, or size — built for desktop and iOS (Pythonista). Clean up your Downloads with one command. I know when I get on an asset bender it can get silly!  Contributions welcome and encouraged, this small tool can be built even bigger and cooler - we are looking for those learning or developing past imposter syndrome, to give an introduction to collaboration on GitHub. ⭐Mentors - we'd appreciate ypur support on this journey, and would love your support with reviews, issues, feedback, PR's = and join us in helping others how to collaborate like pros on GitHub.

***

## 💻 Clone This Project in VSCode

1. Open **Visual Studio Code**
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS)
3. Type and select: **Git: Clone**
4. Paste the repo URL:
   
https://github.com/your-username/pysorta.git

5. Choose a folder to save the project
6. Open the folder when prompted

## ✅ You’re now ready to run `pysorta.py` and start organizing!
***


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
- Works on macOS, Windows, Linux, and even iOS/iPadOS (via [Pythonista](http://omz-software.com/pythonista/))
- Zero dependencies — pure Python!
- Fully Open Source

---

## 🚀 How to Use

### 1. Requirements

- Python 3.x
- Optional: [Pythonista](http://omz-software.com/pythonista/) app for iOS/iPadOS. Link to the App Store at the bottom of this ReadMe.

---

### 2. Run the Script

#### 💻 Mac / Windows / Linux

```bash
python pysorta.py
```

Then follow the interactive prompts:

	•	Choose a folder (or leave blank for current)
	•	Select how you’d like to organize: by type, date, or size
 
⸻

 ### 📱 Pythonista on iOS/iPadOS - available on the App Store:

	1.	Download pysorta.py and place in an on-device foldere you know for Pythonista
 	2.      Open the script in [Pythonista](http://omz-software.com/pythonista/) 
	3.	Tap ▶️ Play
	4.	Enter a path like . or full iOS-accessible folder path
	5.	Choose your sorting method

✅ Tip: You can hardcode a path in the script if needed (e.g. directory = Path("/private/...")).

⸻

### 🧩 Customize File Types

#### Add or edit categories in the FILE_CATEGORIES section of the script:
```bash
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "3D Models": [".obj", ".glb", ".fbx"]
}
```
The script will auto-create folders and move matching files into them.

#### 📂 Example Output
```bash
/Downloads
├── Images
│   └── selfie.png
├── Documents
│   └── resume.pdf
├── Code
│   └── tool.py
```
#### Or by date:
```bash
/Downloads
├── 2024-12
│   └── invoice.pdf
├── 2025-06
│   └── demo.mov
```

## 🐍 So again - what is PySorta?

PySorta (short for “Python Sorta Everything”) is a friendly, flexible script to clean up digital messes.
Whether you’re decluttering a Downloads folder or sorting design assets, PySorta helps you do it cleanly and effortlessly.

## 🤝 Contributing

This project is open to the world — whether you’re learning Python, part of our NO IMPOSTER movement (everyone is welcome to contribute and valued) or improving tooling for creators.
You’re invited to:
	•	Add new organization modes
	•	Improve cross-platform behavior
	•	Refactor for performance
	•	Build a GUI (Tkinter, web, or iOS-native)
	•	Translate prompts into other languages

Pull requests and feedback are warmly welcomed, the goal is for all to use proper features of GitHub, and gain the coding discipline through the use of branches. 💬

## There is so so much more we can do with this - ensure you check out our guide on Contributing here: [CONTRIBUTING.md](CONTRIBUTING.md)

***

## 🪪 License

### MIT License

This project is licensed under the [MIT License](LICENSE).  
See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.

You are free to use, modify, distribute, and build on this project — commercially or privately.

Please keep the original author attribution if redistributing. If you're new to this, please read both links!

***

## ✨ A Note from theProject.

This was built as a small but powerful utility by theProject.  If it helped you, taught you something, or made your life easier — that means everything.
Go build cool things. 🌍.  If you feel compelled, please consider joining ouir cause and sonsoring when it becomes available, or simply giving us a star (we've never got one yet!)  It's all about growing ourselves and aiming to share that confidence and fortitude with others, welcoming a vast community that might not feel good enough to be here when they truly are.

***

## 💣 A Manifesto for the Imposters

Forget the degrees. We are theProject., the relentless misfits who learned by hacking code apart memorizing new PASCAL or QBASIC functions in Barnes and Nobles while our mother's shopped. We had to learni through trial and error — the hard way, and not a reccomended way - as we just haven't built the core principles of software development team work. I have relentlessly been fueled by a burning desire for design, innovation, and access to the deep secrets of the tech frontier.

Far too many great minds lurk in the shadows, feeling like they don’t belong — like they’re missing some secret everyone else figured out. The misfits, the imposters.  We at theProject. embrace you. 

We aim to collaborate with any skillset, use real teamwork, and offer real-world support you can’t find in a textbook or YouTube video. No classes behind a paywall here!

We don’t just create; we defy expectations, we build those killer apps we all wanted to - but never had an artist or an engineer.  Make it stop.

We embrace AI as a tool, not a substitute — and prepare the lost for the new frontier. Man-kind didn't turn down the smart phone - trust we need to learn to use tools, not depend on them.  We got you.

### Welcome to theProject.

I look forward to working with you.

***

## Hack the planet.
### 👾 Lithium187 (a name that brings me back)

---

## Apple App Store Link for Pythonista 3

[![Download on the App Store](https://img.shields.io/badge/Pythonista%203-App%20Store-blue.svg?logo=apple)](https://apps.apple.com/us/app/pythonista-3/id1085978097)

***

<p align="center">
  <a href="https://bytheproject.com" target="_blank">
    <img src="theproject.png" alt="theProject. logo" height="70" />
  </a>
</p>












