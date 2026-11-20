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

from models import(
      Project,
      search_projects,
      bubble_sort_name,
      bubble_sort_project_row

  )      
def search_and_sort_menu(projects_list):
# it will allow user to search projects by keyword or sort using bubble sort.
    print("\n Search and Sort Projects ")
    if len(projects_list) ==0:
        print("No projects to search or sort. Please add a project first !")
        return
        print("1. Search by keyword( Name or type )")
        print("2. Sort Alphabetically by name (A to Z)")
        print("3. Sort by current row count( Lowerst to Highest )")  
        sub_choice = input("Choose (1-3): ").strip()

        if sub_choice == "1":
            term = input("Enter SEarch word:")
# Will call the search algorithm from models.py
            results = search_projects(projects_list, term)
            print(f"\nFound {len(results)} matching project(s):")
            view_all_projects(results)
        elif sub_choice == "2":
 # It will call the bubble sort by name from model.py
            sorted_projects - bubblw_sort_name(projects_list)
            print("\nProjects sorted by Name (A to Z): ")
            view_all_projects(sorted_projects)

        elif sub_choice == 3:
# Will call the bubble sort by row from models.py
            sorted_projects = bubble_sort_project_row(projects_list)
            print("\n Projects sorted by Row Count:")
            view_all_projects(sorted_projects)

        else:
            print("Invalid choice! Returning to menu.")

def show_menu():
# Will print the main menu options on the screen.
    print("\n " + "=" * 40)
    print("     Stichcraft Crochet Assistant")
    print("=" * 40)
    print("1. View all Projects")
    print("2. Add a New Project")
    print("3. Use Row Counter (with Undo/Redo)")
    print("4. Search or Sort Projects")
    print("5. Save and Exit")
    print("=" * 40)



