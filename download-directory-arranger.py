import os
import shutil
import datetime

while 1:

    # Calculating current hour, minute, and second
    today = datetime.datetime.today()
    today = str(today)
    current_hour = today[11:13]
    current_minute = today[14:16]
    current_sec = today[17:19]

    # Make sure system only arranges files at 08:00
    if current_hour == "08" and current_minute == "30" and current_sec == "00":

        # Change Directory to Downloads
        os.chdir("/path/to/Downloads")

        # Save all file names in a list
        files = os.listdir(os.getcwd())

        for filename in files:
            # Ignore Directories
            if not os.path.isdir(filename):

                # Select mp3 or wav, or flac files
                if ".mp3" in filename or ".wav" in filename or ".flac" in filename:
                    # Create 'Audio' directory if it doesn't exist
                    if not os.path.exists("Audio"):
                        os.mkdir("Audio")
                    # Move file in 'Audio' directory
                    shutil.move(filename, "Audio")

                # Select mp4 files
                elif ".mp4" in filename:
                    # Create 'Video' directory if it doesn't exist
                    if not os.path.exists("Video"):
                        os.mkdir("Video")
                    # Move file in 'Video' directory
                    shutil.move(filename, "Video")

                # Select pdf files
                elif ".pdf" in filename:
                    # Create 'PDF' directory if it doesn't exist
                    if not os.path.exists("PDF"):
                        os.mkdir("PDF")
                    # Move file in 'PDF' directory
                    shutil.move(filename, "PDF")

                # Select jpg or png files
                elif ".jpg" in filename or "png" in filename:
                    # Create 'Pictures' directory if it doesn't exist
                    if not os.path.exists("Pictures"):
                        os.mkdir("Pictures")
                    # Move file in 'Pictures' directory
                    shutil.move(filename, "Pictures")

                # Select excel  files
                elif ".xls" in filename:
                    # Create 'Excel' directory if it doesn't exist
                    if not os.path.exists("Excel"):
                        os.mkdir("Excel")
                    # Move file in 'Excel' directory
                    shutil.move(filename, "Excel")

                # Select ppt files
                elif ".ppt" in filename:
                    # Create 'Power Point' directory if it doesn't exist
                    if not os.path.exists("Power Point"):
                        os.mkdir("Power Point")
                    # Move file in 'Power Point' directory
                    shutil.move(filename, "Power Point")

                # Select docx files
                elif ".docx" in filename:
                    # Create 'Word Files' directory if it doesn't exist
                    if not os.path.exists("Word Files"):
                        os.mkdir("Word Files")
                    # Move file in 'Word Files' directory
                    shutil.move(filename, "Word Files")

                # Select .java files
                if ".java" in filename or ".class" in filename or ".py" in filename:
                    # Create 'Code' directory if it doesn't exist
                    if not os.path.exists("Code"):
                        os.mkdir("Code")
                    # Move file in 'Code' directory
                    shutil.move(filename, "Code")

                # Select .zip files
                elif ".zip" in filename:
                    # Create 'Zipped Folders' directory if it doesn't exist
                    if not os.path.exists("Zipped Folders"):
                        os.mkdir("Zipped Folders")
                    # Move file in 'Zipped Folders' directory
                    shutil.move(filename, "Zipped Folders")

                # Select .tar.gz and .deb files
                elif ".deb" in filename or ".tar.gz" or ".tar.xz":
                    # Create 'Linux Folders' directory if it doesn't exist
                    if not os.path.exists("Linux Folders"):
                        os.mkdir("Linux Folders")
                    # Move file in 'Linux Folders' directory
                    shutil.move(filename, "Linux Folders")
