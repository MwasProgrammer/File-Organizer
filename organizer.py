import os
import shutil

def organize_junk():
    # Get the currennt path where the script is sitting
    current_dir = os.getcwd()
    print(f"Scanning directory: {current_dir}")

    # 2. Define the 'Rules' - A dictionary mapping Foldernames to extensions
    # Data modeling - organizing how the script thinks.
    DIRECTORIES = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh"],
        "Executables": [".exe", ".msi"]
    }

    # 3. Loop through every file in this folder
    for filename in os.listdir(current_dir):

        # Get the script to skip itself - the modified part for self-exclusion.
        script_name = os.path.basename(__file__)

        # Skip the script itself and any actual folders.
        if filename == script_name or os.path.isdir(filename) or filename == "directory_flattener.py":
            continue

        # Get the extension (e.g ".pdf")
        file_ext = os.path.splitext(filename)[1].lower()    

        # 4. Logic: find where this file belongs.   
        for folder_name, extensions in DIRECTORIES.items():
            if file_ext in extensions:
                # Create the folder if it doesn't exist.
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                    print(f"Created folder: {folder_name}")

                # Move the file into the appropriate folder.
                shutil.move(filename, os.path.join(folder_name, filename))
                print(f"Moved file {filename} to folder {folder_name}")
                #break  # Stop checking other folders once moved.

if __name__ == "__main__":
    organize_junk()
    print(f"Filetypes organized accordingly")