import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

result_data = pd.read_csv("results.csv")

# count pass and fail for each subject
subjects = result_data.columns[1:-2]

pass_fail_count = {"Overall": {"pass" : 0, "fail" : 0}}

for sub in subjects:
    pass_fail_count[sub] = {'pass' : result_data[result_data[sub] >= 40][sub].count(),
                            'fail' : result_data[result_data[sub] < 40][sub].count()}

    pass_fail_count["Overall"]['pass'] += pass_fail_count[sub]['pass']
    pass_fail_count['Overall']['fail'] += pass_fail_count[sub]['fail']


print("\nPass/ Fail count")
print(pd.DataFrame(pass_fail_count))

# scatter plot
sns.scatterplot(x='Science', y = 'English', data = result_data)
plt.title("Scatter plot of Science vs English")
plt.show()

# line chart
pass_fail_df = pd.DataFrame(pass_fail_count)
pass_fail_df.plot(kind = "bar", stacked = True)
plt.title("Pass / Fail for subjects")
plt.xlabel("Subjects")
plt.ylabel("Count")

plt.show()