import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from the result file (replace 'result.csv' with your actual file path)
result_data = pd.read_csv("results.csv")

# Display the top 10 rows of the dataset
print("Top 10 rows of the dataset:")
print(result_data.head(10))

# Count the number of pass and fail for each subject and overall result
subjects = result_data.columns[1:-2]  # Assuming columns from 2nd to second-to-last are subjects
pass_fail_counts = {"Overall": {"Pass": 0, "Fail": 0}}

for subject in subjects:
    pass_fail_counts[subject] = {
        "Pass": result_data[result_data[subject] >= 40][subject].count(),
        "Fail": result_data[result_data[subject] < 40][subject].count(),
    }

    # Update overall pass/fail counts
    pass_fail_counts["Overall"]["Pass"] += pass_fail_counts[subject]["Pass"]
    pass_fail_counts["Overall"]["Fail"] += pass_fail_counts[subject]["Fail"]

# Display pass/fail counts
print("\nPass/Fail Counts:")
print(pd.DataFrame(pass_fail_counts))

# Visualize the data

# Scatter Plot of Subject1 vs Subject2
sns.scatterplot(x="English", y="Science", data=result_data)
plt.title("Scatter Plot of Subject1 vs Subject2")
plt.show()

# Line Chart of Subject-wise Pass/Fail Counts
pass_fail_df = pd.DataFrame(pass_fail_counts).T
pass_fail_df.plot(kind="bar", stacked=True)
plt.title("Pass/Fail Counts by Subject")
plt.xlabel("Subject")
plt.ylabel("Count")
plt.show()

# Bar Chart of Overall Pass/Fail Counts
overall_pass_fail = pd.DataFrame(pass_fail_counts["Overall"], index=["Overall"])
overall_pass_fail.plot(kind="bar", stacked=True)
plt.title("Overall Pass/Fail Counts")
plt.xlabel("Overall")
plt.ylabel("Count")
plt.show()

# Histogram of Total Marks
plt.hist(result_data["Total"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Frequency")
plt.show()
