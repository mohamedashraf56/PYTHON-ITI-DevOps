import os
import shutil
import datetime

# Create a sample directory and file for testing
source_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'lab')
if not os.path.exists(source_dir):
    os.makedirs(source_dir)

sample_file = os.path.join(source_dir, 'sample.txt')
with open(sample_file, 'w') as file:
    file.write('This is a sample file for backup and restore testing.')

# Create the destination folder if it doesn't exist
dest_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'mybackfolder')
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)


def backupData(source, dest):
    # Check if the source path exists
    if not os.path.exists(source):
        print("Source folder does not exist.")
        return

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y-%H%M%S")
    # Create the backup path with the timestamp
    myPath = os.path.join(dest, timestamp)

    # Check if the source is a directory
    if os.path.isdir(source):
        # Copy the directory to the backup path
        shutil.copytree(source, myPath)
        print('Folder backup successfully')
    # Check if the source is a file
    elif os.path.isfile(source):
        # Copy the file to the backup path
        shutil.copy2(source, myPath)
        print('File backup successfully')
    else:
        print('Not a file or directory')


def restoreData(dest, target):
    # Check if the destination directory exists
    if not os.path.exists(dest):
        print("Destination folder does not exist.")
        return

    # Get the list of backup directories in the destination folder
    backup_dirs = os.listdir(dest)
    if not backup_dirs:
        print("No backups found.")
        return

    # Find the most recent backup directory (based on timestamp)
    latest_backup = max(backup_dirs, key=lambda d: datetime.datetime.strptime(d, "%d-%b-%Y-%H%M%S"))
    latest_backup_path = os.path.join(dest, latest_backup)

    # Check if the latest backup is a directory or a file
    if os.path.isdir(latest_backup_path):
        # Restore the directory
        if os.path.exists(target):
            shutil.rmtree(target)
        shutil.copytree(latest_backup_path, target)
        print('Folder restored successfully')
    elif os.path.isfile(latest_backup_path):
        # Restore the file
        shutil.copy2(latest_backup_path, target)
        print('File restored successfully')
    else:
        print('Not a file or directory')


# Backup the data
backupData(source_dir, dest_dir)

# Restore the data to a new target location
restored_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'restored_lab')
restoreData(dest_dir,restored_dir)
