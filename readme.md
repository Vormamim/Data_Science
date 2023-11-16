This Python script primarily leverages the pandas library to manage and process datasets. It deals with a sample fitness dataset and personal fitness records (which can be customized for individual usage).

```
import pandas as pd
from datetime import datetime
```

The libraries required to run this script are imported. pandas is a powerful data handling library, and datetime is used to handle date and time.


```
dataset = pd.DataFrame({
    'bodyPart': ['waist', 'waist', 'waist', 'upper legs', 'waist', 'back', 'lower legs', 'back'],
    'equipment': ['body weight', 'body weight', 'body weight', 'body weight', 'body weight', 'cable', 'body weight', 'body weight'],
    'gifUrl': ['http://d205bpvrqc9yn1.cloudfront.net/0001.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0002.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0003.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1512.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0006.gif', 'http://d205bpvrqc9yn1.cloudfront.net/0007.gif', 'http://d205bpvrqc9yn1.cloudfront.net/1368.gif', 'http://d205bpvrqc9yn1.cloudfront.net/3293.gif'],
    'id': [1, 2, 3, 1512, 6, 7, 1368, 3293],
    'name': ['3/4 sit-up', '45° side bend', 'air bike', 'all fours squad stretch', 'alternate heel touchers', 'alternate lateral pulldown', 'ankle circles', 'archer pull up'],
    'target': ['abs', 'abs', 'abs', 'quads', 'abs', 'lats', 'calves', 'lats']
})
```
A DataFrame 'dataset' is created. It contains information about a set of different exercises such as what body part it targets, the equipment used, gifUrl for the exercise, its unique 'id', the exercise name, and the primary muscle group it targets.


```
personal_records = pd.DataFrame(columns=['Exercise', 'Date', 'Repetitions'])
```
A second empty DataFrame 'personal_records' is initialized. This will store personal fitness records.


```
exercise_name = '3/4 sit-up'
date = datetime.now().strftime("%Y-%m-%d")
repetitions = 15  # Replace with your actual repetitions
```
This specifies a new record that's going to be added in 'personal_records' DataFrame. date is set to the current date. 'repetitions' can be replaced with the actual number of repetitions performed.


```print(type(personal_records))```
The type of the 'personal_records' is printed, which will be <class 'pandas.core.frame.DataFrame'>.

```index = len(personal_records)```

The next free index in 'personal_records' DataFrame is calculated.

```personal_records.loc[index] = [exercise_name, date, repetitions]```
A new row is added at the calculated index to 'personal_records' DataFrame.

```personal_records.to_csv('personal_fitness_records.csv', index=False)```
The 'personal_records' DataFrame is saved to 'personal_fitness_records.csv' file. The 'index=False' argument is to prevent pandas from writing row indices.

```loaded_records = pd.read_csv('personal_fitness_records.csv')```
The 'personal_fitness_records.csv' file is read and stored into 'loaded_records'.

```print(loaded_records)```
Finally, the 'loaded_records' DataFrame is printed to the console.