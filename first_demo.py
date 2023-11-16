import pandas as pd
from datetime import datetime

# Load the dataset into a Pandas DataFrame
dataset = pd.DataFrame({
    'bodyPart': ['waist', 'waist', 'waist', 'upper legs', 'waist', 'back', 'lower legs', 'back'],
    'equipment': ['body weight', 'body weight', 'body weight', 'body weight', 'body weight', 'cable', 'body weight', 'body weight'],
    'gifUrl': ['http://d205bpvrqc9yn1.cloudfront.net/0001.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0002.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0003.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1512.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0006.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0007.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1368.gif', 'http://d205bpvrqc9yn1.cloudfront.net/3293.gif'],
    'id': [1, 2, 3, 1512, 6, 7, 1368, 3293],
    'name': ['3/4 sit-up', '45° side bend', 'air bike', 'all fours squad stretch', 'alternate heel touchers', 'alternate lateral pulldown', 'ankle circles', 'archer pull up'],
    'target': ['abs', 'abs', 'abs', 'quads', 'abs', 'lats', 'calves', 'lats']
})

# Your personal fitness records DataFrame
# Initialize it with columns like 'Exercise', 'Date', 'Repetitions', etc.
personal_records = pd.DataFrame(columns=['Exercise', 'Date', 'Repetitions'])

# Example: Add a record for the first exercise
exercise_name = '3/4 sit-up'
date = datetime.now().strftime("%Y-%m-%d")
repetitions = 15  # Replace with your actual repetitions

print(type(personal_records))

# Get the current length of the DataFrame
index = len(personal_records)

# Add a new row at this index
personal_records.loc[index] = [exercise_name, date, repetitions]

# Save your personal records to a CSV file
personal_records.to_csv('personal_fitness_records.csv', index=False)

# To read the records back
loaded_records = pd.read_csv('personal_fitness_records.csv')

# Display the loaded records
print(loaded_records)
