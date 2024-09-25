import os ,sys
content_updater_path = os.path.abspath("C:/Users/Admin/Documents/VS Code/test projects/[Day 3] README Content Updater")
sys.path.append(content_updater_path)

import readme_update_table as folder_list 
from datetime import date

project_count = len(folder_list.sorted_folder_list)

current_date = date.today()
repo_creation_date = date(2024,9,13) 
# Even tho this repo is created on 09/14 , i consider 9/13 as the creation date since I finished the Day 1 project on that 
# date and I forgot to create this repo on that date.

total_days = current_date - repo_creation_date
total_projects_todo = total_days.days - project_count

print("="*50)
print(f"This repo was created {total_days.days} days ago.")
print("-"*50)
print(f"There are currently {project_count} projects are in the repo but ...")
print(f"there are {total_projects_todo} that are not finished.")
print("="*50)
print(f"This repo has {(project_count/total_days.days *100 ) :.2f}% completion as of {current_date}")