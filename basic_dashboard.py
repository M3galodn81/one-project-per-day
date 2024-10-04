import os, subprocess
from tkinter import Label, Tk, Button

# Get Scripts
parent_folder_path = "c:/Users/Admin/Documents/VS Code/test projects/"
update_readme_folder = "[Day 3] README Content Updater"
repo_quota_folder= "[Day 10] This Repo Quota"
project_maker_folder= "[Day 15] Project Folder Maker"

download_sort_folder= "[Day 1] Download File Organizer"
make_qr_folder= "[Day 13] QR Code Generator"

def update_readme():
    path = os.path.join(parent_folder_path,update_readme_folder)
    subprocess.run(['python',os.path.join(path,'readme_update_table.py')])

def repo_quota():
    path = os.path.join(parent_folder_path,repo_quota_folder)
    subprocess.run(['python',os.path.join(path,'display_quota.py')])

def project_maker():
    path = os.path.join(parent_folder_path,project_maker_folder)
    subprocess.run(['python',os.path.join(path,'project_folder_maker.py')])

def download_sort():
    path = os.path.join(parent_folder_path,download_sort_folder)
    subprocess.run(['python',os.path.join(path,'download_file_organizer.py')])

def qr_maker():
    path = os.path.join(parent_folder_path,make_qr_folder)
    subprocess.run(['python',os.path.join(path,'qr_code_gen.py')])

# UI
root = Tk()
root.title("Repo Dashboard") 
header_text = Label(root, text = "Welcome to Basic Repo Dashboard App")

repo_category_text = Label(root, text = "Repository Related Actions")
update_button = Button(root, text = "Update Repository" , width= 30, command = update_readme)
repo_quota_button = Button(root, text = "Repo Quota" , width= 30, command = repo_quota)
project_maker_button = Button(root, text = "Project Maker" , width= 30, command = project_maker)

other_category_text = Label(root,text = "Other Related Actions")
download_sort_button = Button(root, text = "Download File Organizer" , width= 30, command = download_sort)
qr_maker_button = Button(root, text = "QR Generator" , width= 30, command = qr_maker)

stop_button = Button(root, text = "Stop" , width= 30, command = root.destroy)

header_text.pack()

repo_category_text.pack()
update_button.pack()
repo_quota_button.pack()
project_maker_button.pack()

other_category_text.pack()
download_sort_button.pack()
qr_maker_button.pack()

stop_button.pack()

root.mainloop()