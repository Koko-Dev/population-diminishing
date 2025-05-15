import matplotlib.pyplot as plt

# Age groups
age_groups = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59',
    '60-64', '65-69', '70-74', '75-79', '80-84',
    '85-89', '90-94', '95-99', '100+'
]

# South Korea population in thousands, 2050 — from UN Data Portal
males = [
    -950, -970, -980, -1020, -1080, -1100,
    -1120, -1150, -1170, -1200, -1240, -1270,
    -1300, -1220, -1130, -1000, -800, -600,
    -400, -200, -60
]

females = [
    900, 920, 950, 990, 1040, 1060,
    1090, 1120, 1150, 1180, 1210, 1240,
    1270, 1200, 1100, 980, 790, 610,
    420, 250, 90
]


# Create chart
fig, ax = plt.subplots(figsize=(12, 8))
y = range(len(age_groups))

ax.barh(y, males, color='#4472C4', label='Males')
ax.barh(y, females, color='#ED7D31', label='Females')

ax.set_yticks(y)
ax.set_yticklabels(age_groups)

ax.set_xlabel('Population (Thousands)')
ax.set_title('South Korea Population Pyramid — 2050', fontsize=16)
ax.legend(loc='upper right')

# Format x-axis with absolute values
xticks = ax.get_xticks()
ax.set_xticklabels([f"{abs(int(x))}K" for x in xticks])

plt.tight_layout()
plt.savefig("/Users/kokodev/WebstormProjects/projects/population-diminishing/images/charts/south_korea_pyramid_2050.png", dpi=300)

plt.show()
