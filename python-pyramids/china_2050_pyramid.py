import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Raw data provided by the user
data = {
    "Age": [
        "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39",
        "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79",
        "80-84", "85-89", "90-94", "95-99", "100+"
    ],
    "M": [
        20582914, 22168251, 21857089, 21251827, 21315635, 24045678, 41757180, 47457181,
        44633383, 41725938, 43219667, 49691348, 58411133, 46103908, 37821349, 40441407,
        31824746, 16537541, 5003585, 1081873, 55074
    ],
    "F": [
        19379528, 20840370, 20492676, 19804262, 19522436, 21623096, 36643898, 40912095,
        38141647, 35891461, 37980580, 45343506, 55918905, 46536458, 40307226, 46401808,
        40377803, 24171448, 9569732, 3112889, 330553
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert to numeric type if necessary
df["M"] = pd.to_numeric(df["M"])
df["F"] = pd.to_numeric(df["F"])

# Set figure size and layout
fig, ax = plt.subplots(figsize=(10, 8))

# Plot horizontal bar chart for male (left) and female (right)
y_pos = np.arange(len(df["Age"]))
ax.barh(y_pos, -df["M"], align='center', color='steelblue', label='Male')
ax.barh(y_pos, df["F"], align='center', color='lightcoral', label='Female')

# Format y-axis and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(df["Age"])
ax.invert_yaxis()  # Highest age on top
ax.set_xlabel('Population')
ax.set_title('China Population Pyramid — Projection for 2050')
ax.legend(loc='lower right')

# Format axis ticks
ax.set_xticklabels([f"{abs(int(x/1e6))}M" for x in ax.get_xticks()])

plt.tight_layout()
plt.grid(True, linestyle='--', linewidth=0.5, axis='x')
plt.axvline(0, color='black', linewidth=0.5)

# Save the chart
chart_path = "/Users/kokodev/WebstormProjects/projects/population-diminishing/images/charts/china_pyramid_2050.png"
plt.savefig(chart_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to: {chart_path}")

