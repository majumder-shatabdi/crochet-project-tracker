"""
In accordance with course guidelines for Assessment 1, generative AI 
was used  as an assisted code reviewer to find out errors in the code specially the spacing problems spelling mistakes special characters brackets
which are difficult to find out with naked eyes. All implementation 
decisions, logic, and testing were written and verified by the student.
"""

import storage
from models import(
    Project,
    search_projects,
    bubble_sort_name,
    bubble_sort_project_row
)
from main import(
    calculate_blanket_yarn,
    calculate_cardigan_neck,
    calculate_gauge,
    calculate_muffler_chain,
    estimate_crafting_time
)
def show_menu():
#Will print the menu iption on the screen.
    print("\n" + "=" *40)
    print("      Stichcraft Crochet Assistant")
    print("=" * 40)
    print("1. View all the Projects")
    print("2. Add a new Project")
    print("3. Use the Row Counter with Undo or Redo")
    print("4.Sort the Projects based on alphabets or row count.")
    print("5. Use Crochet Calculators.")
    print("6. Save and Exit")
    print("=" *40)
def view_all_projects(projects_list):
# Will show all existing projects in a list
    print("\n Your saved projects  ")
        
    if len(projects_list)==0:
        print("No projects found. Add a new one to get staarted!")
    for project in projects_list:
        progress = project.get_progress_percentage()
        print(f"Id: {project.project_id} | Name: {project.name} | Type: {project.craft_type}")
        print(f" Row: {project.current_row}/ {project.target_rows} ({progress: .1f}%) | Status: {project.status}")
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


def row_counter(project_list):
# Interactive row counter with live Undo and redo stack operations.
    print("\n Row counter ")
    if len(project_list) == 0:
        print("No projects are available right now. Please add a new Project!")
        return
# Show available projects so user can pick any one
    for p in project_list:
        print(f"ID [{p.project_id}]: {p.name} (Currently on row {p.current_row}/ {p.target_rows})")

    chosen_id = input("\nEnter Project Id you are working on: ").strip()
# Find the choosen project on the list
    selected_project = None
    for p in project_list:
        if p.project_id ==chosen_id:
            selected_project = p
            break
    if selected_project is None:
        print(f"Error: Project ID '{chosen_id}' not found.")
        return
    while True:
        progress= selected_project.get_progress_percentage()
        print("\n" + "-" * 35)
        print(f"Project: {selected_project.name}")
        print(f"Current Row: {selected_project.current_row}/ {selected_project.target_rows}({progress: .1f%})")
        print(f"Status: {selected_project.status}")
        print("-" * 35)
        print("[+] Add Row | [-] Minus Row | [u] Undo | [r] Redo | [b] Back to meain menu")
        action = input("Action: ").strip().lower()
        if action == "+":
            new_count = selected_project.increase_row()
            print(f"-> Row added! Now on row {new_count}.")
        elif action == "-":
            new_count= selected_project.decrease_row()
            print(f"-> Row reduced! Now on row {new_count}.")
        elif action == "u":
            new_count = selected_project.undo_row()
            print(f"-> Action Undone! Restored to row {new_count}.")
        elif action == "r":
            new_count = selected_project.new_row()
            print(f"-> Action Redone! Moved forward to row{new_count}.")
        elif action == "b":
            storage.save_projects(project_list)
            print("\nRow progress saved. Returning to main menu.")
            break
        else:
            print("Invalid Input!  Use +, -, u, r, or b.")
def search_sort_menu(projects_list):
# Will allow user to search projects by keyword using bubble sort algorithm
    print("\n Search and Sort Projects")
    if len(projects_list) == 0:
        print("No projects to search or sort. Please add a project first!")
        return
    
    print("1. Search by Keyword (Name or Craft Type)")
    print("2. Sort Alphabatically by Name (A to Z)")
    print("3. Sort by Row count (Lowest to Highest)")
    sub_choice = input("Choose (1 - 3): ").strip()

    if sub_choice == "1":
        term = input("Enter search word: ").strip()
        results = search_projects(projects_list, term)
        print(f"\nFound {len(results)} matching project :")
        view_all_projects(results)

    elif sub_choice == "2":
        sorted_projects = bubble_sort_name(projects_list)
        print("\nProjects are Sorted by Name: (A to Z) :")
        view_all_projects(sorted_projects)
    elif sub_choice == "3":
        sorted_projects = bubble_sort_project_row(projects_list)
        print("\nProjects are sorted by Row Count : ")
        view_all_projects(sorted_projects)
    else:
        print("Invalid Choice! Returning to main menu.")


def calculator():
# This menu will allow user to run the calculations of crochet.
    while True:
        print("\n" + "" *40)
        print("    Crochet Calculators")
        print("=" * 40)
        print("1.Granny Square Blanket Calculator")
        print("2. Cardigan Neck Split Calculator")
        print("3. Universal Gauge Calculator")
        print("4. Muffler / Scarf Chain Calculator")
        print("5. Crafting Time Calculator")
        print("6. Back to Main Menu")
        print("=" * 40)
        choice = input("Choose a calculator (1 - 6 ):").strip()
        if choice == "1":
            print("\n Blanket & Yarn Calculator")
            try:
                w =float(input("Enter blanket width (inches): "))
                l = float(input("Enter blanket lencgth (inches): "))
                result = calculate_blanket_yarn(w,l)
                print(f"Total Granny Squares needed : {result['total_squares']}")
                print(f"Total Yarn Weight : {result['total_yarn_grams']} grams")
                print(f"50 gm Milk Cotton Yarn balls needed : {result['balls_needed']} balls")
            except ValueError as e:
                print(f" Error:{e}")
        elif choice == "2":
            print(" Cardigan Neck Split Calculator ")
            try:
                chain = int(input("Enter total neck foundation chains :"))
                result = calculate_cardigan_neck
                print(f"Back: {result['back']} stiches")
                print(f"Left Front: {result['left_front']} stiches")
                print(f"Right Front: {result['right_front']} stiches")
                print(f"Shoulders: {result['left_shoulder']} on each shoulder")
                print(f"Total check : {result['total']} stiches preserved!")
            except ValueError as e:
                print(f"Error:{e}")

        elif choice == "3" :
            print("\n Universal Gauge Calculator")
            try:
                dim= float(input("Enter swatch dimension (e.g. 4.0 inches or 10.0 cm)"))
                stich = int(input("Enter the number of stiches you counted in swatch:"))
                rows = int(input("Enter number of rows counted in swatch: "))
                result = calculate_gauge(dim, stich, rows)
                print(f" Stiches Per Unit : {result['stiches_per_unit']}")
                print(f"Rows per Unit: {result['rows_per_unit']}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            print("\n Muffler / Scarf CHain Calculator")
            try:
                length_muffler = float(input("Enter desired scarf length(inches or cm): "))
                width_swatch = float(input("Enter desired width of swatch (inches or cm): "))
                swatch_stiches = int(input("Enter stiches counted in that swatchwidth: "))
                chains = calculate_muffler_chain(length_muffler, width_swatch, swatch_stiches)
                print(f"Foundation chains to make: {chains} chains ")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("\n Crafting Time Estimator ")
            try:
                total_stiches = int(input("Enter total stiches in project: "))
                speed = int(input("Enter stiches per minute (default 20) : "))
                result = estimate_crafting_time(total_stiches, speed)
                print(f"Estimated Time: {result['formatted']} ({result['total_minutes']}) total minutes")
            except ValueError as e:
                print(f"Error: {e}") 
        elif choice =="6":
            print("Returning to main Menu:")
            break
        else:
            print("Invalid Choice! PLease type a number from 1 to 6.")





def main():
# Main loop loading to show menu and projects
    projects_list = storage.load_projects()
    while True:
        show_menu()
        choice = input("Please choose an option ( 1 - 5 )").strip()
        if choice == "1":
            view_all_projects(projects_list)
        elif choice == "2":
            add_new_project(projects_list)
        elif choice == "3":
            row_counter(projects_list)
        elif choice == "4":
            search_sort_menu(projects_list)
        elif choice == "5":
            calculator()
        elif choice =="6":
            storage.save_projects(projects_list)
            print("\nAll projects are saved safely. Goodbye and Happy Crafting!")
            break
        else:
            print("\nInvalid choice! PLease type a Number from 1 to 5.")
if __name__ == "__main__":
        main()