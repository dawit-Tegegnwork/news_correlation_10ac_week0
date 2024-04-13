import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data
data = pd.read_csv('data.csv')

# Display first few rows
print(data.head())


# Check columns
print(data.columns)

# Get summary statistics
print(data.describe())

# Visualize data (e.g., distribution of categories)
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=data)
plt.title('Distribution of Categories')
plt.xticks(rotation=45)
plt.show()