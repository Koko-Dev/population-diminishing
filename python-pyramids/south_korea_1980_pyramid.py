import matplotlib.pyplot as plt

# Age groups
age_groups = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59',
    '60-64', '65-69', '70-74', '75-79', '80-84',
    '85-89', '90-94', '95-99', '100+'
]

# Real 1980 UN data from World Population Prospects
# Male population (negated for left side of pyramid)
males = [
    -2055484, -2356336, -2330956, -2266452, -2154956,
    -1594808, -1324290, -1165392, -1105853, -862435,
    -618445, -532125, -376736, -264335, -163966, -76808,
    -33144, -10226, -1339, -70, -2
]

# Female population
females = [
    1892109, 2181328, 2163716, 2107383, 2027984,
    1519121, 1223759, 1105462, 1057871, 897600,
    714276, 599081, 447513, 359577, 262893, 155777,
    87801, 33118, 9217, 1309, 61
]

# Build the pyramid chart
fig, ax = plt.subplots(figsize=(12, 8))
y = range(len(age_groups))

# Plot bars
ax.barh(y, males, color='#4472C4', label='Males')
ax.barh(y, females, color='#ED7D31', label='Females')

# Aesthetics
ax.set_yticks(y)
ax.set_yticklabels(age_groups)

ax.set_xlabel('Population')
ax.set_title('South Korea Population Pyramid — 1980', fontsize=16)
ax.legend(loc='upper right')

# Format x-axis to show absolute values in millions
xticks = ax.get_xticks()
ax.set_xticklabels([f"{abs(int(x)) // 1_000_000}M" for x in xticks])

# Save the chart
plt.tight_layout()
plt.savefig("/Users/kokodev/WebstormProjects/projects/population-diminishing/images/charts/south_korea_pyramid_1980.png", dpi=300)
plt.show()
