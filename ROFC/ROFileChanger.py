# Wrillen by SynapLink private project by t.me/damniewa
# Write t.me/damniewa to join us
# The file does not need manual. It is logically understandable

import os
import shutil

config_file = "config.txt"

# Loading files from files_to_change.txt file
def load_files_to_change():
    try:
        with open("files_to_change.txt", "r") as file:
            files = [line.strip() for line in file if line.strip()]
        return files
    except FileNotFoundError:
        print("File 'files_to_change.txt' is missing!")
        return []

# Load Roblox textures path from file
def load_path():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return file.read().strip()
    return r"C:\Program Files (x86)\Roblox\Versions\version-8794089906d54893\content\textures"

# Save Roblox textures path to file
def save_path(path):
    with open(config_file, "w") as file:
        file.write(path)

# Ensure directories exist
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Replace Roblox files with local files
def replace_files(texpath):
    files_list = load_files_to_change()
    ensure_dir("temp")

    for rel_path in files_list:
        roblox_file = os.path.join(texpath, rel_path)
        local_file = os.path.join("textures", rel_path)
        temp_file = os.path.join("temp", rel_path)

        ensure_dir(os.path.dirname(temp_file))

        # Если оригинальный файл Roblox существует, переносим его в temp
        if os.path.exists(roblox_file):
            shutil.move(roblox_file, temp_file)
        else:
            print(f"Roblox file '{rel_path}' missing. Skipped backup.")

        # Если локальный файл существует, копируем его в Roblox
        if os.path.exists(local_file):
            shutil.copy(local_file, roblox_file)
            print(f"Replaced '{rel_path}'.")
        else:
            print(f"Local texture '{rel_path}' missing. Skipped replacement.")

# Restore original Roblox files from backup and save current to textures
def restore_files(texpath):
    files_list = load_files_to_change()

    for rel_path in files_list:
        roblox_file = os.path.join(texpath, rel_path)
        temp_file = os.path.join("temp", rel_path)
        local_texture_file = os.path.join("textures", rel_path)

        ensure_dir(os.path.dirname(local_texture_file))

        # Перемещаем изменённый файл Roblox обратно в textures
        if os.path.exists(roblox_file):
            shutil.move(roblox_file, local_texture_file)
            print(f"Moved changed file '{rel_path}' back to textures.")

        # Восстанавливаем оригинал из temp обратно в Roblox
        if os.path.exists(temp_file):
            shutil.move(temp_file, roblox_file)
            print(f"Restored original Roblox file '{rel_path}'.")
        else:
            print(f"No backup found for '{rel_path}'. Skipped restore.")

texpath = load_path()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Roblox File Changer by SynapLink project")
    print(f"Current Roblox Path: {texpath}\n")

    print("Select an option:")
    print("0 - Change Roblox Path")
    print("1 - Replace Files")
    print("2 - Restore Original Files")

    try:
        ch = int(input("Your choice: "))
    except ValueError:
        input("Invalid input! Press Enter to retry.")
        continue

    if ch == 0:
        texpath = input("Enter Roblox Textures Path: ").strip()
        save_path(texpath)
        print("Path updated.")
        input("Press Enter to restart...")

    elif ch == 1:
        ensure_dir("textures")
        replace_files(texpath)
        input("Files replaced! Press Enter to continue.")

    elif ch == 2:
        restore_files(texpath)
        input("Files restored! Press Enter to continue.")

    else:
        input("Invalid choice! Press Enter to retry.")
