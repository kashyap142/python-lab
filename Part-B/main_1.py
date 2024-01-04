import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Function to read data from CSV or Excel file
def read_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")


# Function to scatter plot all points
def scatter_plot(data, x_label, y_label):
    plt.scatter(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"Scatter Plot of {x_label} vs {y_label}")
    plt.show()


# Function to calculate mean
def calculate_mean(data):
    return np.mean(data)


# Function to calculate median
def calculate_median(data):
    return np.median(data)


# Function to calculate standard deviation
def calculate_std_dev(data):
    return np.std(data)


# Function to calculate variance
def calculate_variance(data):
    return np.var(data)


# Function to calculate slope and intercept for regression line
def calculate_regression_line(data, x_label, y_label):
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        data[x_label], data[y_label]
    )
    return slope, intercept


# Function to draw regression line
def draw_regression_line(data, x_label, y_label):
    slope, intercept = calculate_regression_line(data, x_label, y_label)
    plt.scatter(data[x_label], data[y_label])
    plt.plot(
        data[x_label],
        slope * data[x_label] + intercept,
        color="red",
        label="Regression Line",
    )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"Regression Line of {x_label} vs {y_label}")
    plt.legend()
    plt.show()


# Example usage
file_path = "your_data_file.csv"  # Replace with your actual file path
x_label = "Label_X"
y_label = "Label_Y"

data = read_data(file_path)

scatter_plot(data, x_label, y_label)

mean_value = calculate_mean(data[y_label])
median_value = calculate_median(data[y_label])
std_dev_value = calculate_std_dev(data[y_label])
variance_value = calculate_variance(data[y_label])

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")
print(f"Variance: {variance_value}")

draw_regression_line(data, x_label, y_label)
