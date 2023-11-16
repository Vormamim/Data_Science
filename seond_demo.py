import pandas as pd
from datetime import datetime
import tkinter as tk

#create a window
window = tk.Tk()
window.title("Fitness Tracker")
window.geometry("400x400")



# Load the dataset into a Pandas DataFrame
dataset = pd.DataFrame({
    'bodyPart': ['waist', 'waist', 'waist', 'upper legs', 'waist', 'back', 'lower legs', 'back'],
    'equipment': ['body weight', 'body weight', 'body weight', 'body weight', 'body weight', 'cable', 'body weight', 'body weight'],
    'gifUrl': ['http://d205bpvrqc9yn1.cloudfront.net/0001.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0002.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0003.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1512.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0006.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0007.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1368.gif', 'http://d205bpvrqc9yn1.cloudfront.net/3293.gif'],
    'id': [1, 2, 3, 1512, 6, 7, 1368, 3293],
    'name': ['3/4 sit-up', '45° side bend', 'air bike', 'all fours squad stretch', 'alternate heel touchers', 'alternate lateral pulldown', 'ankle circles', 'archer pull up'],
    'target': ['abs', 'abs', 'abs', 'quads', 'abs', 'lats', 'calves', 'lats']
})

# create a drop down menu of body parts
bodyPart = tk.StringVar(window)
bodyPart.set("Body Part") # default value

# Get unique body parts from the dataset
unique_body_parts = dataset['bodyPart'].unique()

#pack the drop down menu
bodyPartMenu = tk.OptionMenu(window, bodyPart, *unique_body_parts)

#pack the window
bodyPartMenu.pack()

#main loop
window.mainloop()