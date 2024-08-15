import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Set the seed for reproducibility of random numbers
np.random.seed(42)

# Create lists to store the data
common_names = ["John", "Maria", "Constantine", "Eleni", "Dimitris", "Anna", "Panagiotis", "Sophia", "Nikolaos", "Vasiliki", "George",
                "Petros", "Elpida", "Julia", "Areti", "Isidoros", "Anastasios", "Katerina"]
names = []
ages = []
grades = []

# Generate random data for 10 students
for _ in range(10):
    while True:
        name = random.choice(common_names)
        if name not in names:
            names.append(name)
            break

    # Generate a random age between 18 and 25
    age = np.random.randint(18, 26)
    ages.append(age)

    # Generate a random grade between 0 and 100
    grade = np.random.randint(0, 101)
    grades.append(grade)

# Create the DataFrame
students_df = pd.DataFrame({'Name': names, 'Age': ages, 'Grade': grades})

# Filter the DataFrame for students aged 20 and with a grade above 50
filtered_df = students_df[(students_df['Age'] == 20) & (students_df['Grade'] > 50)]

# Calculate the mean grade from the filtered DataFrame
mean_grade = filtered_df['Grade'].mean()

# Select the 'Age' column
ages_1 = students_df['Age']
# Define age bins with a step of three
bins = [18, 20, 23, 26]
# Create the histogram
ages_1.plot(kind='hist', bins=bins, edgecolor='black')
# Add titles and labels
plt.title('Age Distribution of Students')
plt.xlabel('Age')
plt.ylabel('Number of Students')
# Display the histogram
plt.show()
