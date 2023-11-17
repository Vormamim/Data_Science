import tkinter as tk
import pandas as pd

dataset = pd.DataFrame({
    'bodyPart': ['waist', 'waist', 'waist', 'upper legs', 'waist', 'back', 'lower legs', 'back'],
    'equipment': ['body weight', 'body weight', 'body weight', 'body weight', 'body weight', 'cable', 'body weight', 'body weight'],
})

window = tk.Tk()
window.title("Fitness Tracker")
window.geometry("400x400")

unique_body_parts = list(dataset['bodyPart'].unique())
unique_equipment = list(dataset['equipment'].unique())

bodyPartLabel = tk.Label(window, text="Select a Body Part")
bodyPartLabel.pack()

bodyPart = tk.StringVar(window)
bodyPart.set("PLEASE SELECT A BODY PART")
bodyPartMenu = tk.OptionMenu(window, bodyPart, *unique_body_parts)
bodyPartMenu.pack()

exerciseLabel = tk.Label(window, text="Select an Exercise")
exerciseLabel.pack()

equipment = tk.StringVar(window)
equipment.set(unique_equipment[0]) 
equipmentMenu = tk.OptionMenu(window, equipment, *unique_equipment)
equipmentMenu.pack()

def update_equipment_list(*args):
    selected_body_part = bodyPart.get() 
    filtered_dataset = dataset[dataset['bodyPart'] == selected_body_part] 
    equipment_list = filtered_dataset['equipment'].unique()
    
    # Clear the current options from the equipment OptionMenu
    equipmentMenu["menu"].delete(0, "end")
    
    for equip in equipment_list:
        equipmentMenu["menu"].add_command(label=equip, command=tk._setit(equipment, equip))

bodyPart.trace('w', update_equipment_list)

window.mainloop()
