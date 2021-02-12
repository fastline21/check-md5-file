import hashlib
import os
from glob import glob
import platform
import subprocess

# Star program
print("Starting program...")

# Check current directory
check_dir_path = input("Directory: ")

# Printing your choose directory
print(f"Your directory to check files is {check_dir_path}")

# Current dir
current_dir = ''.join(check_dir_path.split('\\')[-1:])

# Current md5
current_md5 = f"{check_dir_path}\\{current_dir}.md5"

# Empty result hash list
result_hash = []

# List all content of check current directory
result_content = os.listdir(check_dir_path)

# Count files
count = 0

# Initial value of is_files
is_files = "file"

# Read check dir path loop
for root, dirs, files in os.walk(check_dir_path):
    for file in files:
        # List of files under check dir path
        with open(os.path.join(root, file), "r") as auto:

            # Open file
            with open(auto.name, "rb") as f:
                # Hashing file
                file_hash = hashlib.md5()
                while chuck := f.read(8192):
                    file_hash.update(chuck)

                # Remove check dir path in current dir
                current_dir = auto.name.replace(check_dir_path + "\\", "")

                # Result hash
                result = f"{file_hash.hexdigest()} *{current_dir}"

                # Increment count
                count += 1

                # Printing count and result
                print(count, result)

                # Append the result in result hash
                result_hash.append(result)

# If more than 1 count
if count >= 1:
    is_files = "files"

# Count of check files.
print(f"Finish check files. You got {count} {is_files}.")

# Write in md5 file
with open(current_md5, "w") as filehash:
    for content_hash in result_hash:
        filehash.write("%s\n" % content_hash)

# Open folder message
print(f"Opening the folder of location {current_md5}.md5")

# Open folder by Platform used
if platform.system() == "Windows":
    os.startfile(check_dir_path)
elif platform.system() == "Darwin":
    subprocess.Popen(["open", check_dir_path])
else:
    subprocess.Popen(["xdg-open", check_dir_path])

# Close program
print("Stopping program... Thank you :)")
