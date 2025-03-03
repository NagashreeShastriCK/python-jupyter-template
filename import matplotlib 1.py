import matplotlib.pyplot as plt

# Step 1: Define the data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Step 2: Define colors for each bar
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Step 3: Create the bar plot
plt.bar(categories, values, color=colors, width=0.6)

# Step 4: Label the axes
plt.xlabel('Categories')
plt.ylabel('Values')

# Step 5: Give the plot a title
plt.title('Bar Plot with Custom Colors')

# Step 6: Add data labels on top of each bar
for i, value in enumerate(values):
    plt.text(i, value + 0.1, str(value), ha='center')

# Step 7: Optionally add grid lines
plt.grid(axis='y', alpha=0.5)

# Step 8: Display the plot
plt.show()