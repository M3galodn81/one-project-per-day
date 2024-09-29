import os,sys,datetime

sys.stdout.reconfigure(encoding='utf-8')
parent_folder = "c:/Users/Admin/Documents/VS Code/test projects/"
os.chdir(parent_folder)

folder_list = []
for item in os.listdir(os.getcwd()):
    if os.path.isdir(os.path.join(os.getcwd(),item)) and item.startswith("[Day "):
        folder_list.append(item)

latest_day = len(folder_list)
folder_name = f"[Day {latest_day+1}] "

print("=======================  Project Maker  =======================")
while True:
    try:    
        project_name = input(f"Enter your project name: ")

        for char in project_name:
            if char in ['<','>',':','"','/','\\''|','?','*']:
                raise Exception("The name contains a illegal character.")

        if project_name[-1] in [" ","."]:
            print("Windows will not allowed a directory name with a space or dot")
            continue
        
        folder_name = folder_name + project_name
        os.mkdir(os.path.join(parent_folder,folder_name))
        break

    except Exception as e:
        print("Error: " + str(e))
        project_name = ""
        continue

project_file_name = project_name.replace(" ","_").lower() + ".py"
project_file_path = os.path.join(parent_folder,folder_name,project_file_name)

os.chdir(os.path.join(parent_folder,folder_name))
print(os.path.join(parent_folder,folder_name))

with open(project_file_path, 'w') as file:
    file.write(f"# {project_name} : Created on {datetime.date.today()}")

print(f"The project folder for {project_name} has been made.")
print("======================== END =======================")