# Roblox File Changer

Created by SynapLink Project  
Support & Feedback: [t.me/damniewa](https://t.me/damniewa)

---

## Overview

This program allows users to manage and replace Roblox texture files with custom textures and restore the original textures afterward. The program is open source, and anyone can use it freely. Users who have trust concerns can independently verify the code and scan it for viruses.

---

## File Structure

Your program folder should have the following structure:

```
RobloxFileChanger/
│
├── main.py
├── LAUNCH.bat
├── config.txt (auto-generated)
├── files_to_change.txt
├── textures/
│   └── (custom textures)
└── temp/ (auto-generated)
```

---

## Setup & Usage

### Step 1: Setting Roblox Path

- Launch the program using `LAUNCH.bat` to ensure proper permissions.
- Select option `0` to specify the Roblox textures folder path.
- Example path: `C:\Program Files (x86)\Roblox\Versions\your-version\content\textures`

Note: The specified path will be automatically saved for future use.

### Step 2: Preparing Textures

- Place custom textures in the `textures` folder, matching Roblox's file structure.

Example:
```
textures/
├── MouseLockedCursor.png
└── Cursors/
    └── Cursor.png
```

### Step 3: Specifying Files to Change

- Open `files_to_change.txt`.
- Add each file path (relative to the Roblox textures folder) intended for replacement:

```
MouseLockedCursor.png
Cursors\Cursor.png
```

### Step 4: Replacing Files

- Select option `1` in the program.
- The program will:
  1. Back up original Roblox files into the `temp` folder.
  2. Replace Roblox files with custom textures from the `textures` folder.

### Step 5: Restoring Original Files

- Select option `2` in the program when ready to restore.
- The program will:
  1. Move modified Roblox files back into the `textures` folder.
  2. Restore original Roblox textures from the `temp` folder.

---

## Important Notes

- Use "Replace Files" functions while in game so Roblox does not run Update Check.
- Run Roblox from Roblox Player not from website.
- When you close the Roblox make sure to use "Restore Files" function so next time roblox does not update the version, and you dont have to change Roblox path again.
- Always restore original files before updating or reinstalling Roblox to avoid potential errors.
- Launch the program exclusively through `LAUNCH.bat` to ensure sufficient privileges.
- Contact support ([t.me/damniewa](https://t.me/damniewa)) for any assistance.

---

Happy customizing.

