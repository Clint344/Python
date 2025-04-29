# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})

# Task 1: Load and Explore the Dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

print("\nMean of features grouped by species:")
print(df.groupby("species").mean())

# Task 3: Visualizations

# Set seaborn style
sns.set(style="whitegrid")

# 1. Line chart (not typical for iris, but we’ll use index to simulate trend)
plt.figure(figsize=(8, 4))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Sepal and Petal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(6, 4))
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(6, 4))
plt.hist(df["sepal width (cm)"], bins=15, color="salmon")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter plot: Sepal vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="deep")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Findings
print("\nObservations:")
print("- Setosa has the smallest petal lengths and widths.")
print("- Versicolor and Virginica are closer in measurements.")
print("- Sepal and petal lengths tend to be positively correlated.")
