#Bar chart

import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize

categories = np.array(["grains", "Fruit", "Vegetables", "Protein", "dairy", "Sweets"])
values = np.array([4,3,2,5,3,1])

fig, axes = plt.subplots(1,2, figsize=(12,5))

# --- Left Subplot: Vertical Bar Chart ---
axes[0].bar(categories, values, color="skyblue")
axes[0].set_title("Daily Consumption (Vertical Bar)")
axes[0].set_xlabel("Food")
axes[0].set_ylabel("Quantity")
plt.barh(categories, values, color="Skyblue")

# Note: For barh, the x and y axes are swapped compared to bar
axes[1].barh(categories, values, color="skyblue")
axes[1].set_title("Daily Consumption (Horizontal Bar)")
axes[1].set_xlabel("Quantity")
axes[1].set_ylabel("Food")

plt.tight_layout()
plt.savefig("two_separate_bar_charts.png")



plt.show()