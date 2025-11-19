#Pie
import matplotlib.pyplot as plt
import numpy as np


categories = np.array(["Freshman", "Sophomore", "Junior", "Senior"])
values = np.array([300,250,275,225])
colors = ["red", "yellow", "blue","Pink"]

plt.pie(values, labels=categories, autopct="%1.1f%%", colors=colors, explode=[0,0,0,.1], shadow=True, startangle=180)

plt.title("Northwest Christian School")
plt.show()