import os
import sys

# Reconfigure stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# cd to downloads folder
os.chdir('c:/Users/Admin/Downloads')

# create folders
audio_folder = 'c:/Users/Admin/Downloads/Audio Folder/'
photo_folder = 'c:/Users/Admin/Downloads/Photo Folder/'
video_folder = 'c:/Users/Admin/Downloads/Video Folder/'
exe_folder = 'c:/Users/Admin/Downloads/EXE Folder/'
other_folder = 'c:/Users/Admin/Downloads/Other Format Folder/'

if os.path.exists(audio_folder):
    print(f'The audio folder is already created')
else:
    os.mkdir(audio_folder)
    print(f'Created Audio Folder')

if os.path.exists(photo_folder):
    print(f'The photo folder is already created')
else:
    os.mkdir(photo_folder)
    print(f'Created Photo Folder')

if os.path.exists(video_folder):
    print(f'The video folder is already created')
else:
    os.mkdir(video_folder)
    print(f'Created Video Folder')

if os.path.exists(exe_folder):
    print(f'The exe folder is already created')
else:
    os.mkdir(exe_folder)
    print(f'Created EXE Folder')

if os.path.exists(other_folder):
    print(f'The other format folder is already created')
else:
    os.mkdir(other_folder)
    print(f'Created Other Format Folder')

# scan each item and get their extension
file_list = []
main_directory = r'C:\Users\Admin\Downloads'

for file_path in os.listdir(main_directory):
    try:
        if os.path.isfile(os.path.join(main_directory, file_path)):
            file_list.append(file_path)

            file_info = os.path.splitext(file_path)
            file_extension = file_info[1]

            # put the file into the respective folder
            if file_extension in ['.mp3','.flac','.wav','.ogg']: 
                os.rename(os.path.join(main_directory, file_path),os.path.join(main_directory,'Audio Folder', file_path))
                print(f'{file_path} has been moved to the Audio Folder')

            elif file_extension in ['.png','.bmp','.jpg','.gif','.svg']: 
                os.rename(os.path.join(main_directory, file_path),os.path.join(main_directory,'Photo Folder', file_path))
                print(f'{file_path} has been moved to the Photo Folder')

            elif file_extension in ['.mp4','.avi','.mov']: 
                os.rename(os.path.join(main_directory, file_path),os.path.join(main_directory,'Video Folder', file_path))
                print(f'{file_path} has been moved to the Video Folder')

            elif file_extension in ['.exe','.rar','.zip','.msi']: 
                os.rename(os.path.join(main_directory, file_path),os.path.join(main_directory,'EXE Folder', file_path))
                print(f'{file_path} has been moved to the EXE Folder')

            else:
                os.rename(os.path.join(main_directory, file_path),os.path.join(main_directory,'Other Format Folder', file_path))
                print(f'{file_path} has been moved to the Other Format Folder')


    except UnicodeEncodeError:
        print(f"Error encoding file: {file_path}")

    except FileExistsError:
        print(f"{file_path} already exists. Will skip moving the file.")
        continue

print("All the files are in the folders")

