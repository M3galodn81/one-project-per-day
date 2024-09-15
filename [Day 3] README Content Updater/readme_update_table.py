import os
import sys
import re
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')
os.chdir('c:/Users/Admin/Documents/VS Code/test projects/')
# print(os.getcwd())

# Scan the folders
# check if folder and check if folder has [Day prefix
folder_list = []
for item in os.listdir(os.getcwd()):
    if os.path.isdir(os.path.join(os.getcwd(),item)) and item.startswith("[Day "):
        folder_list.append(item)

def extract_day(folder):
    match = re.search(r'\[Day (\d+)\]', folder)  #(\d+) catch any digits 
    return int(match.group(1))

sorted_folder_list = sorted(folder_list, key = extract_day) #sort the list based on the digits catch from the function extract_day

# Markdown Gen
md_output = []
main_link = "https://github.com/M3galodn81/one-project-per-day/tree/main/"

md_output.append("### All Projects\n")
md_output.append("| Time | Project           |\n")
md_output.append("| ---- | ----------------- |\n")

# generate link and save it into a iter var
for x in sorted_folder_list:
    folder_parsed = urllib.parse.quote(x)

    day = f"{re.search(r'\[Day (\d+)\]', x).group(0)}"
    folder_link = f"[{x.split("] ", 1)[1]}]({main_link}{folder_parsed})"

    md_output.append(f"| {day} | {folder_link} |\n")

md_output.append("\n<p align=\"right\"><a href=\"#readme-top\">(back to top)</a></p>")

# Modify the current README.md

md_path = "README.md"
banner = "<!-- Update -->" 

with open(md_path,'r') as file:
     lines = file.readlines()

for line_number, line in enumerate(lines, start=1):
    if banner in line:
        keep_contents = lines[:line_number]
        keep_contents.extend(md_output)
        break

with open(md_path,'w') as file:
    file.writelines(keep_contents)