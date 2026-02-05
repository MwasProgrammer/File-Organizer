import os
import shutil

def flatten_directory():
    current_dir = os.getcwd()
    print(f"Flattening directory in {current_dir}")

    script_name = os.path.basename(__file__)

    for root, dirs, files in os.walk(current_dir):    
        print(f"Scanning directory: {root}")
        print(f"Found {len(files)} files.") 
        print(f"Found {len(dirs)} directories.")

        if '.git' in dirs:
           dirs.remove('.git')  # Skip the .git directory

        if root == current_dir:
            continue  # Skip the current directory itself

        for filename in files:
            if filename ==script_name:
                continue  # Skip the script itself

            source_path = os.path.join(root, filename) # Full path to the file
            destination_path = os.path.join(current_dir, filename) # Destination path in the current directory

            # Handle potential filename conflicts
            if os.path.exists(destination_path):
                print(f"Warning: {filename} already exists. Skip or rename the file.")
            else:
                try:
                    print(f"Moving file {filename} from {source_path} to {destination_path}")
                    shutil.move(source_path, destination_path)

                except Exception as e:
                    print(f"Error moving file {filename}: {e}")

        print(f"Directory flattened successfully.")

if __name__ == "__main__":
    flatten_directory()