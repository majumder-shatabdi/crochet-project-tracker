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
from main import(
calculate_blanket_yarn,
calculate_cardigan_neck,
calculate_gauge,
calculate_muffler_chain,
estimate_crafting_time
)
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
notebook.add(tab_projects, text = " Project Management ")
tab_counter = tk.Frame(notebook)
notebook.add(tab_counter, text = " Row Counter ")
tab_calculator = tk.Frame(notebook)
notebook.add(tab_calculator, text = " Calculators ")

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
    storage.save_projects(project_list)
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

# Tab for Crochet calculators and logic
calculator_title =tk.Label(tab_calculator, text = "Crochet Calculators", font = ("Arial", 14, "bold"))
calculator_title.pack(pady=5)

# First section : Blanket and Yarn balls Calculator
blanket_frame= tk.LabelFrame(tab_calculator, text = "Granny Square Blanket Calculator", font = ("Arial", 10,"bold"), padx= 10, pady=5)
blanket_frame.pack(fill="x",padx =15, pady=5)
tk.Label(blanket_frame, text = "Width (in): ").grid(row=0, column = 0, padx=3, pady=2)
calculator_blanket_w = tk.Entry (blanket_frame, width = 8)
calculator_blanket_w.grid(row=0,column = 1, padx= 3, pady = 2)

tk.Label(blanket_frame, text = "Length (in): ").grid(row=0, column = 2, padx = 3, pady = 2)
calculator_blanket_l = tk.Entry(blanket_frame, text = " Squares : - | Balls: - ", font = ("Arial", 9, "bold"), fg="#198754")
calculator_blanket_l.grid(row=0,column=3,padx=3, pady=2)

blanket_result_lbl = tk.Label(blanket_frame, text = "Squares : - | Balls: - ", font=("Arial", 9 , "bold"), fg = "#198754")
blanket_result_lbl.grid(row=0, column =5, padx = 10, pady=2)

def calculator_blanket():
    try:
        width = float(calculator_blanket_w.get().strip())
        length= float(calculator_blanket_l.get().strip())
        result = calculate_blanket_yarn(width,length)
        blanket_result_lbl.config(text=f"Squares: {result['total_squares']} | 50g balls: {result['balls_needed']}")
    except ValueError as e:
        messagebox.showerror("Calculation Error", str(e))
tk.Button(blanket_frame, text="Calculate", command =calculator_blanket, bg ="#e2e3e5").grid(row=0,column=4,padx=5,pady=2)


# Cardigan neck split calculator
cardigan_frame = tk.LabelFrame(tab_calculator,text="Cardigan Neck Split (Preserving the base chain)", font=("Arial", 10, "bold"), padx=10, pady=5)
cardigan_frame.pack(fill="x", padx= 15, pady= 5) 
tk.Label(cardigan_frame,text="Base chains (min 30): ").grid(row=0,column=0,padx=3,pady=2)
calculate_cardigan_chain = tk.Entry(cardigan_frame, width= 8)
calculate_cardigan_chain.grid(row=0, column= 1, padx=3, pady=2)

cardigan_result_lbl = tk.Label(cardigan_frame, text = "Back : - | Front : - | Each Shoulder : - ", font=("Arial",9, "bold"), fg="#0678fd")
cardigan_result_lbl.grid(row=1,column=0,columnspan=4, sticky="w", padx=5, pady=3)
def calculator_cardigan():
    try:
        chains= int(calculate_cardigan_chain.get().strip())
        result = calculate_cardigan_neck(chains)
        cardigan_result_lbl.config(
            text=f"Back: {result['back']} st | Front : {result['left_front']} & {result['right_front']} st | Shoulders: {result['left_shoulder']}| Total: {result['total']}"
        )
    except ValueError as e:
        messagebox.showerror("Calculation Error:" , str(e))

tk.Button(cardigan_frame, text = "Calculate", command = calculator_cardigan, bg = "#e2e3e5").grid(row=0,column = 2, padx=5, pady =2)

# Crafting time estimation
time_frame = tk.LabelFrame(tab_calculator, text = " Crafting Time Estimator ", font = ("Arial", 10, "bold"), padx=10, pady = 5)
time_frame.pack(fill="x", padx=15, pady=5)
tk.Label(time_frame, text = "Total Stiches: ").grid(row=0, column = 0, padx = 3, pady = 2)
calculator_time_sts= tk.Entry(time_frame, width =8)
calculator_time_sts.grid(row=0, column=1, padx=3, pady=2)

tk.Label(time_frame, text = "Speed (stiche / min):").grid(row=0, column = 2, padx=3, pady = 2)
calculator_time_speed= tk.Entry(time_frame, width=8)
calculator_time_speed.insert(0, "20")
calculator_time_speed.grid(row=0, column = 3, padx = 3, pady = 2)

time_result_lbl= tk.Label(time_frame, text = "Estimated Time: ", font=("Arial", 9, "bold"), fg = "#6f42c1")
time_result_lbl.grid(row=0, column = 5, padx=10, pady=2)


def calculation_time():
    try:
        total_stich= int(calculator_time_sts.get().strip())
        speed = int(calculator_time_speed.get().strip())
        result = estimate_crafting_time(total_stich,speed)
        time_result_lbl.config(text=f"Time: {result['formatted']} {result['total_minutes']} mins)")
    except ValueError as e:
        messagebox.showerror("Calculate Error", str(e))

tk.Button(time_frame, text = "Estimate", command = calculation_time, bg ="#e2e3e5").grid(row=0,column= 4, padx=5, pady=2)

refresh_project_listbox()
if __name__ =="__main__":
    root.mainloop()


