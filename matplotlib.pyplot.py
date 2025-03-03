import matplotlib.pyplot as plt

# Data for the plots
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
categories = ['A', 'B', 'C', 'D']
values = [5, 3, 9, 6]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [10, 15, 7, 5]

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# First subplot: Line plot
axs[0, 0].plot(x, y, marker='o', linestyle='-', color='b')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')

# Second subplot: Bar plot
axs[0, 1].bar(categories, values, color='orange')
axs[0, 1].set_title('Bar Plot')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')

# Third subplot: Scatter plot
axs[1, 0].scatter(x, y, color='green')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')

# Fourth subplot: Pie chart
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Pie Chart')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()