import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility (optional)
np.random.seed(42)

# Generate random x and y arrays
x_values = np.random.uniform(0, 1000, 100)
y_values = np.random.uniform(0, 50, 100)

# Create a scatter plot
plt.scatter(x_values, y_values, label='Random Data')

# Add arrows
for i in range(len(x_values)):
    plt.arrow(x_values[i], y_values[i], 10, 2, head_width=10, head_length=2, fc='red', ec='red')

# Add labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Random X-Y Plot with Arrows')

# Add legend
plt.legend()

# Display the plot
plt.show()
