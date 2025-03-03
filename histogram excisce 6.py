import matplotlib.pyplot as plt

# Define the data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

# Create the histogram
plt.figure(figsize=(8, 5))  # Optional: Set the figure size
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

# Add a title and labels
plt.title('Customized Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()