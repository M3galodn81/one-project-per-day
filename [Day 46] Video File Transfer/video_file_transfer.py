import os
import sys
import shutil 

sys.stdout.reconfigure(encoding = 'utf-8')

video_folder = 'c:/Users/Admin/Videos'
transfer_folder = 'd:/Old Videos'

os.chdir(video_folder)

video_list = []

for file_path in os.listdir(video_folder):
    try:
        if os.path.isfile(os.path.join(video_folder,file_path)):
            video_list.append(file_path)

            # os.rename(os.path.join(video_folder, file_path),os.path.join(transfer_folder, file_path))
            shutil.move(os.path.join(video_folder, file_path),os.path.join(transfer_folder, file_path))
            print(f'{file_path} has been moved to the D drive')

    except UnicodeEncodeError:
        print(f"Error encoding file: {file_path}")

    except FileExistsError:
        print(f"{file_path} already exists. Will skip moving the file.")
        continue

print("All the files are in the D drive")