import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv')

# Perform analysis
# Example: Calculate mean and plot a histogram
mean = data['column'].mean()
plt.hist(data['column'], bins=20)
plt.title('Histogram of Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
