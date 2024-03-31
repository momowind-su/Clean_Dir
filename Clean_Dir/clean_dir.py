import os
import datetime

def delete_old_files(directory, days=7):
    # Get the current time
    now = datetime.datetime.now()

    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file's last modified time
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            # Check if the file is older than the specified number of days
            if (now - file_modified_time).days > days:
                print(f"Deleting file: {file_path}")
                os.remove(file_path)  # Delete the file

# Usage
user_directory_path = input("Enter the path of the directory to clean up: ")
delete_old_files(user_directory_path)


