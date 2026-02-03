# File-Organizer
A python automated script that organizes files into folders based on their file extensions e.g document files with .pdf, .docx extensions are automatically stored in Documents folder.

 **Status:** Version 1.1 (Stable) - Logic refined for self-exclusion and sequential execution.

---

# Features
* **Self-Awareness:** The script identifies its own filename and excludes itself from being moved.
* **Smart Categorization:** Automatically sorts files into categorized folders:
    * Documents (`.pdf`, `.docx`, `.txt`, `.xlsx`)
    * Images (`.jpg`, `.png`, `.gif`)
    * Videos (`.mp4`, `.mkv`)
    * Scripts (`.py`, `.js`, `.sh`)
    
* **Infrastructure Safety:** Checks for folder existence before creation to prevent directory errors.
* **Idempotent Logic:** Can be run multiple times without causing duplicate folders or errors.

---

# How It Works
The script follows a specific logic flow to ensure no files are lost or misplaced:
1. **Identify Path:** Gets the current working directory.
2. **Self-Exclusion:** Stores the script name to avoid moving itself.
3. **Loop & Filter:** Scans all items, skipping directories and the script itself.
4. **Match & Move:** Matches file extensions against a pre-defined data model and moves them to the appropriate destination.

---

# Installation & Usage

1. **Clone the repository:**
   git clone https://github.com/MwasProgrammer/File-Organizer.git

2. **Navigate to the folder:**
    cd File-Organizer

3. **Run the script:**
    python organizer.py