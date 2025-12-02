import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("pokemon.csv")
type1_count = (df["Type1"].value_counts(ascending=True))

plt.barh(type1_count.index, type1_count, color="#9BB591", edgecolor="black")
plt.title("# of Pokemon Type 1")
plt.ylabel("Type")
plt.xlabel("Count")

plt.tight_layout()


plt.show()