import os
import shutil

def file_cleaner():
    print(f"Welcome to the File Cleaner!")

    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")

    script_name = os.path.basename(__file__)

    DIRECTORY ={
        "Trash":[".tmp", ".log"]
    }

    for filename in os.listdir(current_directory):
        file_extension = os.path.splitext(filename)[1]

        # Check if the file extension matches any in the DIRECTORY
        for folder_name, extensions in DIRECTORY.items():
            # If the file extension matches, move the file to the corresponding folder
            if file_extension in extensions:
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                    print(f"Created folder: {folder_name}")

                # Move the file to the folder
                shutil.move(filename, os.path.join(folder_name, filename))
                print(f"Moved file: {filename} to folder: {folder_name}")

    for root, dirs, files in os.walk(current_directory):
        if '.git' in dirs:
            dirs.remove('.git')  # Exclude .git directory from traversal

        if 'SecretVault' in dirs:
            dirs.remove('SecretVault')  # Exclude SecretVault directory from traversal

        if 'PROJECTARCHIVE' in dirs:
            dirs.remove('PROJECTARCHIVE')  # Exclude PROJECTARCHIVE directory from traversal

        print(f"Directory: {root}"
              f"\nSubdirectories: {dirs}"
              f"\nFiles: {files} size: {sum(os.path.getsize(os.path.join(root, f)) for f in files)} bytes\n")
        
        # To get the size of each file 
        for filename in files:
            file_size = os.path.getsize(os.path.join(root, filename))
            print(f"File: {filename} size: {file_size} bytes\n")


        
        if script_name in files:
            files.remove(script_name)  # Exclude the script itself from traversal

            
        ARCHIVEDIR ={
            "PROJECTARCHIVE": ["OLD"]
        }

        # Check the size of each file and move it to the PROJECTARCHIVE folder if it's larger than 1KB
        # 1KB = 1000 bytes
        
            
        for filename in files:
            if os.path.getsize(os.path.join(root, filename)) > 1000 or filename.startswith("OLD"):
                print(f"File: {filename} is larger than 1KB, moving to PROJECTARCHIVE.")
                # Create the PROJECTARCHIVE folder if it doesn't exist
                if not os.path.exists("PROJECTARCHIVE"):
                    os.mkdir("PROJECTARCHIVE")
                    print(f"Created folder: PROJECTARCHIVE")
                # Move the file to the PROJECTARCHIVE folder
                shutil.move(os.path.join(root, filename), os.path.join("PROJECTARCHIVE", filename))

if __name__ == "__main__":
    file_cleaner()
    print(f"Moved {len(os.listdir('Trash'))} files to the Trash folder.")
    print(f"Moved {len(os.listdir('PROJECTARCHIVE'))} files to the PROJECTARCHIVE folder.")