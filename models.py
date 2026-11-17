class Project:
#A single crochet project like baby blanket where project information can be tracked, row counters and can use undo and redo stackif any row is done by mistake.
    def __init__(
        self,
        project_id,
        name,
        type,
        target_rows,
        hook_size= "4.0 mm",
        notes= ""    
    ):
        self.project_id = project_id
        self.name = name
        self.type = type
        self.target_rows = target_rows
        self.current_row = 0
        self.status = "In progress"
        self.hook_size = hook_size
        self.notes = notes
#Using python list for row couter using list
        self.undo_stack =[]
        self.new_stack =[]


    def increse_row(self):
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
                self.status = "In progress"

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
        "type" : self.type,
        "target_rows" : self.target_rows,
        "current_row" : self.current_row,
        "status": self.status,
        "hook_size": self.hook_size,
        "notes": self.notes

    }




