"""
GenAI Acknowledgment (Assessment 1 - Gen-AI-Assisted Reviewer):
In compliance with Keele University academic integrity policies and module guidelines,
generative AI (Google Gemini) was utilized strictly as an automated code reviewer. 
The tool assisted in identifying syntax typos, unhandled cases, and logical errors (such as rounding drift in garment splits and dictionary key mismatches). 
All code structures,  logic, algorithmic decisions, and test cases were written
(Help of Ai was taken on how to write these test cases and how to check that on terminal but the calculations and logic was given by Shatabdi),
 understood, and verified by Shatabdi Majumder. 
"""
class Project:
#A single crochet project like baby blanket where project information can be tracked, row counters and can use undo and redo stackif any row is done by mistake.
    def __init__(
        self,
        project_id,
        name,
        craft_type,
        target_rows,
        hook_size= "4.0 mm",
        notes= ""    
    ):
        self.project_id = project_id
        self.name = name
        self.craft_type = craft_type
        self.target_rows = target_rows
        self.current_row = 0
        self.status = "In Progress"
        self.hook_size = hook_size
        self.notes = notes
#Using python list for row couter using list
        self.undo_stack =[]
        self.new_stack =[]


    def increase_row(self):
# Increases row by 1 and will record this state to undo stack.
        self.undo_stack.append(self.current_row)
        self.current_row += 1
    # Clearing new stack because of new move was made.
        self.new_stack =[]
    #Stopping criteria
        if self.current_row >= self.target_rows:
           self.status ="Completed"

        return self.current_row

# Decreases the current row by 1. But the value should be never negative.
    def decrease_row(self):
        if self.current_row> 0:
            self.undo_stack.append(self.current_row)  
            self.current_row -=1
            self.new_stack = []
            if self.current_row< self.target_rows:
                self.status = "In Progress"

        return self.current_row
 

    def undo_row(self):
# Reverts the rowcounter value to the previous existing value in the undo stack if user makes one wrong row.
        if len(self.undo_stack) > 0 :
# To Save current row to new stack
            self.new_stack.append(self.current_row)
# takeout the previous row from the undo stack
            previous_row = self.undo_stack.pop()
            self.current_row = previous_row

# Update the new status
            if self.current_row >= self.target_rows:
                self.status = "Completed"
            else:
                self.status = "In Progress"
        return self.current_row
# Re-applies undo row value from the new stack


    def new_row(self):
        if len(self.new_stack) > 0:
            self.undo_stack.append(self.current_row)
# Pop the forward row from new stack
            next_row = self.new_stack.pop()
            self.current_row = next_row
#Update the status
            if self.current_row >= self.target_rows:
                self.status = "Completed"
            else:
                self.status = "In Progress"

        return self.current_row

    def get_progress_percentage(self):
# The percentage calculation of the project
        if self.target_rows <= 0:
            return 0.0
        percentage = (self.current_row/ self.target_rows) * 100.00
        return percentage

# Convert the information into a dictionary for json format

    def dictionary(self):
        return{
        "project_id": self.project_id,
        "name" : self.name,
        "craft_type" : self.craft_type,
        "target_rows" : self.target_rows,
        "current_row" : self.current_row,
        "status": self.status,
        "hook_size": self.hook_size,
        "notes": self.notes

    }

# Search Algorithm
def search_projects(projects_list, search_term):
# Search process for projects by matching search items inside the project name or craft type 
    search_term =search_term.strip().lower()
    matching_projects = []
    for project in projects_list:
        name_lower = project.name.lower()
        type_lower= project.craft_type.lower()
        if search_term in name_lower or search_term in type_lower:
            matching_projects.append(project)
    return matching_projects

# ALgorithm for sorting using buble sort
def bubble_sort_name(project_list):
# This will sort the projects name based on the alphabets a to z
    sorted_list = list(project_list)
    n =len(sorted_list)
    for i in range(n):
        for j in range(0, n- i -1):
            name1= sorted_list[j].name.lower()
            name2= sorted_list[j+1].name.lower()

            if name1> name2:
                temp = sorted_list[j]
                sorted_list[j]= sorted_list[j+1]
                sorted_list[j+1] = temp

    return sorted_list

# This will sort the projects based on the current row count lowest to highest using buble sort
def bubble_sort_project_row(project_list):
    sorted_list = list(project_list)
    n = len(sorted_list)
    for i in range(n):
        for j in range (0,n-i-1):
            if sorted_list[j].current_row > sorted_list[j+1].current_row:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j+1]
                sorted_list[j+1] = temp
    return sorted_list
