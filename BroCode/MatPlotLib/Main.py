import matplotlib.pyplot as mp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([2023, 2024,2025,2026])
y = np.array([15,25,30,20])

mp.plot(x,y, marker="^")



data2 = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
data1 = [3.5,5.2,7.8,10.5,15.1,22.0,28.5,35.4,41.2,48.9]
y2 = [55, 150, 75, 190, 40, 110, 60, 145, 70, 180]
y3= np.array([2, 4, 5, 7, 8, 10, 11, 13, 14, 15])

#Internet speed data
yearX = np.array(data2)
yearY = np.array(data1)
data3 = np.array(y2)

plt.title("Class size", fontsize= 20, family = "Arial", fontweight= "bold", color = "#859ECC")
plt.xlabel(" Year", fontsize = 20, color="#859ECC")
plt.ylabel(" Class Size", fontsize = 20, color="#859ECC")



line_style = dict(marker= "o", markersize = 10,  # .  , o v ^  < > * h H + X x
                  markerfacecolor="blue",
                  markeredgecolor="red",  #mec
                  linestyle="dotted",
                  linewidth =3,
                  color = "#CFACD9")
                                            #can be abbreviated to ms
mp.plot(yearX, yearY ,marker= "o", markersize = 10,  # .  , o v ^  < > * h H + X x
        markerfacecolor="blue",
        markeredgecolor="red",  #mec
         linestyle="dotted",
        linewidth =3,
        color = "#CFACD9") #


#plt.xticks(yearX)
plt.tick_params(axis='both', colors="#063891" )


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12)) # 3 rows, 1 column

ax1.plot(x, y, marker="^", color="black", linestyle='-')
ax1.set_title("1. General Trend (x, y)")
ax1.set_xlabel("Year", fontsize=12) # Use ax.set_xlabel instead of plt.xlabel
ax1.set_ylabel("Value", fontsize=12)


# --- 2. Plot Internet Speed and Latency on ax2 ---
# We can put these two related time series on the same plot (ax2)
ax2.plot(yearX, yearY, label="Internet Speed (Mbps)", **line_style)
ax2.plot(yearX, y2, label="ML Latency (ms)", marker='x', linestyle='--', color='purple')
ax2.set_title("2. Internet Speed & ML Latency Over Time")
ax2.set_xlabel("Year")
ax2.set_ylabel("Metric Value")
ax2.legend()

# --- 3. Plot Study Hours on ax3 ---
# Since y3 is only 10 points long and has no explicit X-axis, we use a simple index (0-9)
ax3.plot(np.arange(len(y3)), y3, label="Study Hours", color='green', marker='s')
ax3.set_title("3. Study Hours Data (By Index)")
ax3.set_xlabel("Observation Index")
ax3.set_ylabel("Study Hours")

# Adjusts spacing between plots to prevent overlap
plt.tight_layout()

# Display the single figure containing all three graphs
plt.show()


