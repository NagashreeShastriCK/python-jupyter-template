import matplotlib.pyplot as plt

# Step 1: Creating the lists of x-values and y-values
x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]

# Step 2: Plotting the data with customizations
plt.plot(x_values, y_values, color='blue', linestyle='--', marker='o', linewidth=2, markersize=8, label='y = x^2')

# Step 3: Labeling the axes
plt.xlabel('x')
plt.ylabel('y')

# Step 4: Giving the plot a title
plt.title('Customized Line Plot')

# Step 5: Adding a grid
plt.grid(True)

# Step 6: Adding a legend
plt.legend()

# Displaying the plot
plt.show()