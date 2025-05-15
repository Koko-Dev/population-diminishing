import matplotlib.pyplot as plt

# Age groups
age_groups = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59',
    '60-64', '65-69', '70-74', '75-79', '80-84',
    '85-89', '90-94', '95-99', '100+'
]

# South Korea 2023 — estimated population in thousands
males = [
    -970, -990, -1030, -1060, -1100, -1110,
    -1140, -1200, -1250, -1290, -1330, -1300,
    -1250, -1100, -950, -780, -600, -400,
    -200, -80, -20
]

females = [
    930, 950, 1000, 1040, 1080, 1100,
    1130, 1190, 1240, 1280, 1320, 1310,
    1270, 1140, 1000, 850, 700, 520,
    260, 110, 40
]

# Create the pyramid chart
fig, ax = plt.subplots(figsize=(12, 8))
y = range(len(age_groups))

# Plot male and female bars
ax.barh(y, males, color='#4472C4', label='Males')
ax.barh(y, females, color='#ED7D31', label='Females')

# Labeling and aesthetics
ax.set_yticks(y)
ax.set_yticklabels(age_groups)

ax.set_xlabel('Population (Thousands)')
ax.set_title('South Korea Population Pyramid — 2023', fontsize=16)
ax.legend(loc='upper right')

# Format x-axis with absolute values
xticks = ax.get_xticks()
ax.set_xticklabels([f"{abs(int(x))}K" for x in xticks])

# Layout and export
plt.tight_layout()
plt.savefig("/Users/kokodev/WebstormProjects/projects/population-diminishing/images/charts/south_korea_pyramid_2023.png", dpi=300)
plt.show()
