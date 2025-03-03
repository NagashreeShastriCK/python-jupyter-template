import matplotlib.pyplot as plt

# Step 1: Define the data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Step 2: Define colors for each bar
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Step 3: Create the bar plot
plt.bar(categories, values, color=colors)

# Step 4: Label the axes
plt.xlabel('Categories')
plt.ylabel('Values')

# Step 5: Give the plot a title
plt.title('Bar Plot with Custom Colors')

# Step 6: Display the plot
plt.show()