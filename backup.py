import os
import shutil
from datetime import datetime

def is_accessible(folder):
    """Check if folder is accessible."""
    try:
        os.listdir(folder)  # Try to list the files in the folder
        return True
    except PermissionError:
        return False

def create_backup(source_folder, destination_folder):
    """
    Creates a timestamped backup of the source folder inside the destination folder.
    """
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(destination_folder, f"backup_{timestamp}")

    try:
        # Loop through source folder and back up only accessible folders
        for foldername in os.listdir(source_folder):
            folder_path = os.path.join(source_folder, foldername)
            if os.path.isdir(folder_path) and is_accessible(folder_path):
                backup_folder_path = os.path.join(backup_folder, foldername)
                shutil.copytree(folder_path, backup_folder_path)
                print(f"✅ Backed up: {foldername}")
            else:
                print(f"❌ Skipping: {foldername} (Access Denied)")

        print(f"✅ Backup completed successfully at: {backup_folder}")
    except Exception as e:
        print(f"❌ Failed to create backup: {e}")

if __name__ == "__main__":
    # 🔧 Replace with your actual folders
    source = r"C:\Users\Shaikh\Documents"
    destination = r"D:\Backups"

    create_backup(source, destination)
