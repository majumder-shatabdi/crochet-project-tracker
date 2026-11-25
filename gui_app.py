"""
GenAI Acknowledgment (Assessment 1 - Assisted Reviewer):
In compliance with Keele University academic integrity policies, I used 
generative AI (Google Gemini) strictly as an assisted code reviewer and debugger. 
I consulted the tool to help diagnose runtime exceptions (such as Tkinter TclError 
and NameError), identify subtle typographical errors that were difficult to spot 
manually (e.g., grid parameter misspellings and geometry string syntax), and check 
function execution flow. All core logic, project architecture, functional decisions, 
and final code implementations were independently written, tested, and verified by me.

— Shatabdi Majumder
"""

import tkinter as tk
from tkinter import ttk, messagebox
import storage
from models import Project
# Setup and data loading
root = tk.Tk()
root.title("StichCraft - Crochet Assistant")
root.geometry("650x550")
# For loding the existing saved projects
project_list = storage.load_projects()
# Tab Navigation Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill= "both", expand = True, padx = 10, pady = 10)
# First Tab for project management
tab_projects= tk.Frame(notebook)
notebook.add(tab_projects, text = "Project Management")

title = tk.Label(tab_projects, text = "Your Saved Projects", font=("Arial", 14, "bold"))
title.pack(pady=5)
# Visual listbox of projects
project_listbox = tk.Listbox(tab_projects, height = 7, width= 70, font= ("Courier", 9))
project_listbox.pack(padx=10, pady= 5)

separator_project = ttk.Separator(tab_projects, orient = "horizontal")
separator_project.pack(fill = "x", padx = 15, pady= 10)
from_title = tk.Label(tab_projects, text = "Create New Project", font= ("Arial", 12,"bold"))
from_title.pack(pady=5)
from_frame = tk.Frame(tab_projects)
from_frame.pack(pady=5)
# Entry Boxes
tk.Label(from_frame, text="Project Name: ").grid(row=0, column=0, sticky="e", padx=5, pady=3)
entry_name = tk.Entry(from_frame, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=3)

tk.Label(from_frame,text="Craft Type:").grid(row=1,column=0,sticky="e",padx=5,pady=3)
entry_type=tk.Entry(from_frame,width=30)
entry_type.grid(row=1,column=1,padx =5,pady=3)

tk.Label(from_frame, text="Target Rows: ").grid(row=2, column=0, sticky="e", padx=5, pady=3)
entry_rows = tk.Entry(from_frame, width=30)
entry_rows.grid(row=2,column=1,padx=5,pady=3)

tk.Label(from_frame, text="Hook size: ").grid(row=3,column=0,sticky = "e", padx = 5, pady=3)
entry_hook=tk.Entry(from_frame, width=30)
entry_hook.insert(0,"4.0 mm")
entry_hook.grid(row=4,column= 1,padx=5,pady=5)
entry_hook.grid(row=3, column=1, padx=5, pady=3)

tk.Label(from_frame, text="Enter notes: ").grid(row=4, column=0, sticky="e", padx=5, pady=3)
entry_notes = tk.Entry(from_frame, width=30)
entry_notes.grid(row=4, column=1, padx=5, pady=3)
#3.Functions
def refresh_project_listbox():
# Will clear and reload the projects into the visual list.
    project_listbox.delete(0, tk.END)
    for p in project_list:
        progress= p.get_progress_percentage()
        display_text = f"[{p.project_id}] {p.name} ({p.craft_type}) - Row: {p.current_row}/{p.target_rows} ({progress:.1f}%) [{p.status}]"
        project_listbox.insert(tk.END, display_text)

def add_p_click():
# Will read the input box ,create new projects, saves and refreash screen.
    name= entry_name.get().strip()
    craft_type = entry_type.get().strip()
    target_str= entry_rows.get().strip()
    hook = entry_hook.get().strip()
    notes= entry_notes.get().strip()

    if name =="":
        messagebox.showerror("Input Error", "PLease enter a Project name!")
        return
    try:
        target_rows = int(target_str)
        if target_rows<=0:
            messagebox.showerror("input Error", "PLease enter a valid whole number for rows!")
            return
    except ValueError:
        messagebox.showerror("Input Error", "PLease enter a valid whole number for rows!")
        return
    if hook == "":
        hook = "4.0 mm"
    new_id = str(len(project_list) +1)
    new_project= Project(
        project_id =new_id,
        name= name,
        craft_type = craft_type,
        target_rows= target_rows,
        hook_size= hook,
        notes = notes)
    project_list.append(new_project)
    storage.save_project(project_list)
    refresh_project_listbox()

    entry_name.delete(0,tk.END)
    entry_hook.delete(0,tk.END)
    entry_rows.delete(0,tk.END)
    entry_type.delete(0,tk.END)
    entry_notes.delete(0,tk.END)
    messagebox.showinfo("Success", f"Project '{name}' created and saved!")
#4. For attaching button comand and run
button = tk.Button(tab_projects, text="Add Project", font=("Arial", 10, "bold"), bg="#d1e7dd", command=add_p_click)
button.pack(pady=10)
# To fill listbox with saved projects on start

refresh_project_listbox()
if __name__ =="__main__":
    root.mainloop()


