import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# China 2100 Projection Data
china_2100_data = {
    "Age": [
        "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39",
        "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79",
        "80-84", "85-89", "90-94", "95-99", "100+"
    ],
    "M": [
        10582914, 11168251, 11857089, 11251827, 10115635, 9045678, 8175718, 7745718,
        6463338, 6172593, 5321966, 4969134, 4841113, 3610390, 2782134, 2044140,
        1182474, 653754, 300358, 181873, 55074
    ],
    "F": [
        9379528, 9840370, 9492676, 9804262, 9522436, 8623096, 7643898, 7091209,
        5814164, 5589146, 4798058, 4534350, 4591890, 4653645, 4030722, 3640180,
        2037780, 1417144, 956973, 311288, 33055
    ]
}

# Create DataFrame
df = pd.DataFrame(china_2100_data)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(df["Age"]))

# Plot population data (Male as negative, Female as positive)
ax.barh(y_pos, -df["M"], color='steelblue', label='Male')
ax.barh(y_pos, df["F"], color='lightcoral', label='Female')

# Configure axis and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(df["Age"])
ax.set_xlabel("Population")
ax.set_title("China Population Pyramid — Projection for 2100")
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', axis='x')
ax.legend(loc='lower right')

# Format X-axis tick labels
tick_vals = ax.get_xticks()
ax.set_xticks(tick_vals)
ax.set_xticklabels([f"{abs(int(x/1e6))}M" for x in tick_vals])

# Layout and export
plt.tight_layout()
plt.savefig("/Users/kokodev/WebstormProjects/projects/population-diminishing/images/charts/china_pyramid_2100.png", dpi=300)
plt.show()
