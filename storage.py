import json
import os 
from models import Project

def save_projects(projects_list):
# Saves a list of projects objects into the projects.json file
# If the data folder does not exist data folder needs to be created 
    if not os.path.exists("data"):
        os.makedirs("data")
    list_of_dictionaries=[]
#Loop through which projects convert using dictionary method
    for project in projects_list:
        project_data = project.dictionary()
        list_of_dictionaries.append(project_data)
# To open the file and write the data
    file = open("data/projects.json", "w")
    json.dump(list_of_dictionaries, file, indent = 4)
    file.close()

    return True

def load_projects():
# Reads data of projects.json and converts the saved data back into the project objects.
    file_path= "data/projects.json"
# Checks if the file exists on the computer
    if not os.path.exists(file_path):
        #If the file does not exists, return an empty list
        return []
    # Read the file ousing try and except
    try:
        file = open(file_path, "r")
        raw_list = json.load(file)
        file.close()
    #Rebuild the project objects one by one
        rebuilt_projects = []
        for item in raw_list:
            p = Project(
                project_id= item["project_id"],
                name = item["name"],
                craft_type = item["craft_type"],
                target_rows =item["target_rows"],
                hook_size=item["hook_size"],
                notes =item["notes"]
            )
# Restores the saved row and status
            p.current_row = item["current_row"]
            p.status = item["status"]

# Add to rebuilt list
            rebuilt_projects.append(p)
        return rebuilt_projects
    
    except Exception:
# If the file is empty or corrupted then return an empty list without crashing
        return []
