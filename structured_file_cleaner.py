import os
import shutil

#trash directory configuartion using os.listdir() 
def clean_trash(base_path, trash_map):
    # Iterate through the files in the base path
    moved_count = 0 # Counter to keep track of moved files

    for filename in os.listdir(base_path):
        file_extension = os.path.splitext(filename)[1]
        # Check if the file extension matches any in the trash_map
        for folder_name, extensions in trash_map.items():
            if file_extension in extensions:
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name )
                    print(f"Created folder: {folder_name}")

                # Collision handling: If a file with the same name already exists in the destination folder, append a number to the filename
                destination_path = os.path.join(folder_name, filename)
                counter = 1
                while os.path.exists(destination_path):
                    base_name, ext = os.path.splitext(filename)
                    new_filename = f"{base_name}_{counter}{ext}"
                    destination_path = os.path.join(folder_name, new_filename)
                    counter += 1         

                source_path = os.path.join(base_path, filename) # Get the full path of the source file
                shutil.move(source_path, destination_path) # Move the file to the destination folder
                print(f"Moved file: {filename} to folder: {folder_name}")
                # Increment the moved count
                moved_count += 1
    # After processing all files, return the count of moved files
    return moved_count

# PROJECTARCHIVE directory configuration using os.walk()
def archive_files(base_path, size_threshold_kb = 1, prefix = "OLD"):
    archive_folder = "PROJECTARCHIVE"
    moved_count = 0 # Counter to keep track of moved files

    threshold_bytes = size_threshold_kb * 1024 # Convert KB to bytes

    for root, dirs, files in os.walk(base_path):
        for forbidden_dir in ['.git', 'SecretVault', 'PROJECTARCHIVE', 'Trash']:
            if forbidden_dir in dirs:
                dirs.remove(forbidden_dir)  # Exclude forbidden directories from traversal

        for filename in files:
            if filename == os.path.basename(__file__):
                continue  # Skip the script itself

            filepath = os.path.join(root, filename) # Get the full path of the file
            filesize = os.path.getsize(filepath) # Get the size of the file in bytes

            filesize_is_large = filesize > threshold_bytes 
            filename_is_old = filename.upper().startswith(prefix.upper()) # Check if the filename starts with the specified prefix (case-insensitive)

            if filesize_is_large or filename_is_old:
                if not os.path.exists(archive_folder):
                    os.mkdir(archive_folder)
                    print(f"Created folder: {archive_folder}")

                # Collision handling: If a file with the same name already exists in the destination folder, append a number to the filename
                destination_path = os.path.join(archive_folder, filename)
                counter = 1
                while os.path.exists(destination_path):
                    base_name, ext = os.path.splitext(filename)
                    new_filename = f"{base_name}_{counter}{ext}"
                    destination_path = os.path.join(archive_folder, new_filename)
                    counter += 1         

                source_path = os.path.join(root, filename) # Get the full path of the source file
                shutil.move(source_path, destination_path) # Move the file to the destination folder
                print(f"Moved file: {filename} to folder: {archive_folder}")                        


                moved_count += 1
        
    # After processing all files, return the count of moved files
    return moved_count

def main():
    print("Starting the file cleaner...")

    current_directory = os.getcwd()

    trash_configuration = {
        "Trash": [".tmp", ".log"]
        }
    
    cleaned_trash_count = clean_trash(current_directory, trash_configuration)

    total_archived_files = archive_files(current_directory, size_threshold_kb=1, prefix="OLD")

    print("\n", "-" * 50,  "\n")
    print("File cleaning completed.")
    print("\n", "-" * 50)
    print(f"Finished cleaning. Total files moved to Trash: {cleaned_trash_count}")
    print(f"Total files moved to PROJECTARCHIVE: {total_archived_files}")
    print("\n"+"="*50)

if __name__ == "__main__":
    main()





            