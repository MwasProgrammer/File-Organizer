import os
import shutil

# Collision handling
#Overwrite checker function to prevent overwriting files with the same name in the destination folder
def overwrite_checker(destination_folder, filename):
    base_name, ext = os.path.splitext(filename)
    final_path = os.path.join(destination_folder, filename)
    counter = 1

    # While loop to check if the file already exists in the destination folder
    while os.path.exists(final_path):
        new_filename = f"{base_name}_{counter}{ext}"
        final_path = os.path.join(destination_folder, new_filename)
        counter += 1

    return final_path



#trash directory configuartion using os.listdir() 
def clean_trash(base_path, trash_map):
    # Iterate through the files in the base path
    moved_count = 0 # Counter to keep track of moved files
    skipped_count = 0 # Counter to keep track of skipped files

    for filename in os.listdir(base_path):
        file_extension = os.path.splitext(filename)[1]
        # Check if the file extension matches any in the trash_map
        for folder_name, extensions in trash_map.items():
            if file_extension in extensions:
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name )
                    print(f"Created folder: {folder_name}")

                
                source_path = os.path.join(base_path, filename) # Get the full path of the source file
                destination_path = overwrite_checker(folder_name, filename)

                # Error handling for moving files
                try:
                    shutil.move(source_path, destination_path) # Move the file to the destination folder
                    print(f"Moved file: {filename} to folder: {folder_name}")
                    # Increment the moved count
                    moved_count += 1
                except PermissionError:
                    print(f"Permission denied: {filename}. Skipping this file.")
                    skipped_count += 1
                except Exception as e:
                    print(f"Error moving file: {filename}. Error: {e}")
    # After processing all files, return the count of moved files and skipped files
    return moved_count, skipped_count

# PROJECTARCHIVE directory configuration using os.walk()
def archive_files(base_path, size_threshold_kb = 1, prefix = "OLD"):
    archive_folder = "PROJECTARCHIVE"
    moved_count = 0 # Counter to keep track of moved files
    skipped_count = 0 # Counter to keep track of skipped files

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

                
                source_path = os.path.join(root, filename) # Get the full path of the source file
                destination_path = overwrite_checker(archive_folder, filename)

                # Error handling for moving files
                try:
                    shutil.move(source_path, destination_path) # Move the file to the destination folder
                    print(f"Moved file: {filename} to folder: {archive_folder}")                        

                    moved_count += 1
                except PermissionError:
                    print(f"Permission denied: {filename}. Skipping this file.")
                    skipped_count += 1  
                except Exception as e:
                    print(f"Error moving file: {filename}. Error: {e}")
        
    # After processing all files, return the count of moved files and skipped files
    return moved_count, skipped_count

def main():
    print("Starting the file cleaner...")

    current_directory = os.getcwd()

    trash_configuration = {
        "Trash": [".tmp", ".log",".pdf"]
        }
    
    trash_moved, trash_skipped = clean_trash(current_directory, trash_configuration)

    archive_moved, archive_skipped = archive_files(current_directory, size_threshold_kb=1, prefix="OLD")

    print("\n", "-" * 50,  "\n")
    print("File cleaning completed.")
    print("\n", "-" * 50)
    # Summary table
    #Header
    print(f"{'Category':<20} | {'Moved':<10} | {'Skipped':<10}")
    print(f"{'Trash':<20} | {trash_moved:<10} | {trash_skipped:<10}")
    print(f"{'PROJECTARCHIVE':<20} | {archive_moved:<10} | {archive_skipped:<10}")

    print("\n", "-" * 50)
    print(f"Total files skipped: {trash_skipped + archive_skipped}")
    print(f"Total files moved: {trash_moved + archive_moved}")
    print("\n"+"="*50)

if __name__ == "__main__":
    main()





            