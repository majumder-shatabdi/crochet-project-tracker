import storage
from models import Project
def show_menu():
#Will print the menu iption on the screen.
    print("\n" + "=" *40)
    print("      Stichcraft Crochet Assistant")
    print("=" * 40)
    print("1. View all the Projects")
    print("2. Add a new Project")
    print("3. Save and Exit")
    print("=" *40)
def view_all_projects(projects_list):
# Will show all existing projects in a list
    print("\n Your saved projects  ")
        
    if len(projects_list)==0:
        print("No projects found. Add a new one to get staarted!")
    for project in projects_list:
        progress = project.get_progress_percentage()
        print(f"Id: {project.project_id} | Name: {project.name} | Type: {project.craft_type}")
        print(f" Row: {project.current_row}/ {project.target_rows} {progress: 1f}% | Status: {project.status}")
        print("-" * 35)

def add_new_project(projects_list):
# Asks user for details to create a new project."
    print("\n Create a new project")
    name = input("enter project name:")
    craft_type = input("Enter craft type like blanket, scarf, hat etc. :")
# Safe number input to target the number of rows
    try:
        target_rows = int(input("Enter target number of rows:"))
        if target_rows <=0:
            print("Target number of rows can not be zero or negative. PLease enter a positive number")
            return
    except ValueError:
        print("Please enter a valid positive number for number of rows")
        return

    hook_size = input("Enter the size of the hook (e.g. 3.0mm, 4.0 mm): ") 
    if hook_size.strip() == "" :
        hook_size = "4.0 mm" 
    notes = input("Enter any note (optional): ")
# Generate a simple project id based on the list length
    new_id = str(len(projects_list) + 1 )

# Creates the project using models.py Project class
    new_project = Project(
        project_id =new_id,
        name = name,
        craft_type = craft_type,
        target_rows= target_rows,
        hook_size= hook_size,
        notes = notes
    )      
    projects_list.append(new_project)
# Save immidiately to disk so we don't loose the data
    storage.save_projects(projects_list)
    print(f"\nSuccess! Project'{name}' has been created and saved.")

def main():
# This loop will run until the user choose to exit.
    projects_list = storage.load_projects()
    while True:
        show_menu()
        choice =input("Please choose an option (1-3):").strip()

        if choice=="1":
            view_all_projects(projects_list)
        elif choice =="2":
            add_new_project(projects_list)
        elif choice =="3":
# Saves all the data before closing
            storage.save_projects(projects_list)
            print("\nAll projects saved safely. Goodbye and happy crafting!")
            break
        else: 
            print("\nInvalid choice! Please type 1,2 or 3")
if __name__ =="__main__":
    main()
    
