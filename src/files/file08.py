"""
plot student score
"""

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv('data/students.csv')

x = students['First name']
y = students['Score']

plt.title("My first chart")
plt.xlabel("Student First Name")
plt.ylabel("Score")
plt.plot(x, y)
plt.show()