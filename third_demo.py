import tkinter as tk
import pandas as pd

'''
This demo shows how to load a dataset into a Pandas DataFrame and use it to populate a Listbox.
It also shows how to use a StringVar to update the contents of a Listbox.
It also shows how to use an OptionMenu to filter a dataset.
It also shows how to use trace to call a function whenever a StringVar changes.
'''

# Your dataset here
dataset = pd.DataFrame({
    'bodyPart': ['waist', 'waist', 'waist', 'upper legs', 'waist', 'back', 'lower legs', 'back'],
    'equipment': ['body weight', 'body weight', 'body weight', 'body weight', 'body weight', 'cable', 'body weight', 'body weight'],
})

# Create a new tkinter window
window = tk.Tk()

# Set the title
window.title("Fitness Tracker")

# Set the size
window.geometry("400x400")


# Create a StringVar for the body part
bodyPart = tk.StringVar(window) # Create a StringVar

# Get unique body parts from the dataset
unique_body_parts = list(dataset['bodyPart'].unique()) # Get unique body parts from the dataset

#create a label for the drop down menu
bodyPartLabel = tk.Label(window, text="Select a Body Part")
bodyPartLabel.pack()



# Create an OptionMenu for the body parts




bodyPartMenu = tk.OptionMenu(window, bodyPart, *unique_body_parts)
bodyPartMenu.pack()

# create a label for the exercise drop down menu
exerciseLabel = tk.Label(window, text="Select an Exercise")
exerciseLabel.pack()# Create a Listbox for the equipment

equipmentList = tk.Listbox(window)
equipmentList.pack()

def update_equipment_list(*args): # *args is a special parameter that means "all the other parameters"

    
    # Get the selected body part
    selected_body_part = bodyPart.get() 

    # Filter the dataset based on the selected body part
    filtered_dataset = dataset[dataset['bodyPart'] == selected_body_part] 

    # Get the corresponding equipment
    equipment = filtered_dataset['equipment'].unique()

    # Clear the Listbox
    equipmentList.delete(0, tk.END) # Delete everything from index 0 to the end

    # Insert the equipment into the Listbox
    for item in equipment: # Iterate through the equipment
        equipmentList.insert(tk.END, item) # Insert each item into the Listbox until the end

# Call update_equipment_list whenever the selected body part changes
bodyPart.trace('w', update_equipment_list) # 'w' means "whenever the StringVar changes"

# Set the initial body part
bodyPart.set(unique_body_parts[0]) # Set the initial body part to the first item in the list

# Start the tkinter main loop
window.mainloop()