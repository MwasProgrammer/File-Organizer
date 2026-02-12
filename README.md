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



# Structured File Cleaner
**Version 2.0 (Stable)** – *Advanced workplace sanitization and automated file lifecycle management.*

The **Structured File Cleaner** is a Python-based automation utility designed for **Temporary Workplace Sanitization**. Unlike basic sorters, this script implements a multi-tier logic system to distinguish between immediate "Trash" and long-term "Project Archiving," ensuring a clean and organized workstation with zero manual intervention.

---

## New in Version 2.0
* **Modular Architecture:** Refactored into specialized helper functions for high maintainability and code reuse.
* **Tiered Categorization:** Implements dual-purpose logic:
    * **Trash Cleanup:** Immediate removal of transient files (`.tmp`, `.log`, etc.).
    * **Project Archiving:** Automated backup of large or aged files (prefixed with `OLD_`).
* **Collision Handling:** Integrated `overwrite_checker` to prevent data loss when files share identical names.
* **Execution Observability:** A detailed CLI Summary Table generated post-execution, reporting successful moves vs. skipped files.

---

## Features
* **Error Resilience:** Built-in `try...except` safety nets to handle `PermissionError` (locked files) and system-level `OSError` without crashing.
* **Directory Exclusion:** Uses `os.walk()` with a "Forbidden Directory" filter to protect sensitive folders (e.g., `.git`, `SecretVault`, `Trash`).
* **Self-Awareness:** Automatically identifies and excludes the script itself from operations.
* **Idempotent Design:** Safe to run repeatedly; uses path verification to ensure no redundant folders or circular moves occur.

---

## Logic & Architecture
The script operates as a **State-Aware Engine**:
1.  **Scanning Phase:** Traverses the directory tree using `os.walk()` and `os.listdir()`.
2.  **Conflict Resolution:** Uses the `overwrite_checker` to rename files (e.g., `file_1.pdf`) if a conflict exists in the destination.
3.  **Exception Handling:** Monitors for OS-level locks (e.g., files open in other software) to prevent runtime interruptions.
4.  **Reporting:** Aggregates data from multiple modules to provide a final performance metric in a tabulated format.



---

## Installation & Usage

1. Clone the repository:
   git clone https://github.com/MwasProgrammer/File-Organizer.git

2. Navigate to the folder:
    cd File-Organizer

3. Run the script:
    python structured_file_cleaner.py