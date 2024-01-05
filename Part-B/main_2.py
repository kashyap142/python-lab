import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the database and displaying the top 10 rows
tips_data = pd.read_csv("tips.csv")
print("Top 10 rows of the dataset:")
print(tips_data.head(10))

# Scatter Plot (day vs tip)
sns.scatterplot(x="day", y="tip", data=tips_data)
plt.title("Scatter Plot of Day vs Tip")
plt.show()

# Line Chart (day against tip)
sns.lineplot(x="day", y="tip", data=tips_data, ci=None)
plt.title("Line Chart of Day vs Tip")
plt.show()

# Bar chart with day against tip
sns.barplot(x="day", y="tip", data=tips_data, ci=None)
plt.title("Bar Chart of Day vs Tip")
plt.show()

# Histogram of total_bills
plt.hist(tips_data["total_bill"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Total Bills")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()
