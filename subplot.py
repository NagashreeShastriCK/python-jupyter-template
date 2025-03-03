import matplotlib.pyplot as plt
import numpy as np

# Sample data for the plots
x = np.linspace(0, 10, 100)
y_line = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
bar_categories = ['A', 'B', 'C', 'D']
bar_values = [5, 10, 3, 7]
scatter_x = np.random.rand(10)
scatter_y = np.random.rand(10)

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot a line chart in the first subplot
axs[0, 0].plot(x, y_line, color='blue')
axs[0, 0].set_title('Line Chart')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')

# Plot a bar chart in the second subplot
axs[0, 1].bar(bar_categories, bar_values, color='orange')
axs[0, 1].set_title('Bar Chart')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')

# Plot a scatter plot in the third subplot
axs[1, 0].scatter(scatter_x, scatter_y, color='purple')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X Values')
axs[1, 0].set_ylabel('Y Values')

# Plot a pie chart in the fourth subplot
axs[1, 1].pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Pie Chart')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()


