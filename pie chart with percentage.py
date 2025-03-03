import matplotlib.pyplot as plt

# Step 1: Define the data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]  # Values corresponding to each label
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']  # Colors of the pie segments

# Step 2: Create a pie chart
plt.figure(figsize=(8, 6))  # Optional: set the figure size
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Step 3: Customize the text
plt.setp(autotexts, size=10, weight="bold", color="white")  # Make percentage labels bold and white
plt.setp(texts, size=12)  # Set label size

# Step 4: Give the plot a title
plt.title('Pie Chart with Percentages')

# Step 5: Display the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()