import os
import shutil

def clear_folder(folder_path="temp_images"):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Remove files
        except OSError as e:
            print(f"Error removing {item_path}: {e}")

if __name__ != "__main__":
    print("imported module empty_folder_gen")
else:
    clear_folder()