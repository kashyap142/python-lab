import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_data = pd.read_csv("tips.csv")

print("top 10 rows of dataset")
print(tips_data.head(10))

# day vs tip
sns.scatterplot(data = tips_data, x ="day", y ="tip")
plt.title("plot of day vs tip")

plt.show()


# day vs tip linear
sns.lineplot(x='day', y='tip', data=tips_data, ci=None)
plt.title('Line Chart of Day vs Tip')
plt.show()

# bar chart with day against tip
sns.barplot(x='day', y='tip', data = tips_data, ci = None)
plt.title("plot of day vs tip")
plt.show()


# histogarm of total bill
plt.hist(tips_data['total_bill'], bins = 20, color = 'red', edgecolor = 'black')
plt.title("histogarm of total bills")
plt.xlabel("Total Bill")
plt.ylabel("Freq")

plt.show()