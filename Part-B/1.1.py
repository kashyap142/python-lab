import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import stats


def read_file(file_name):
    if file_name.endswith('.csv'):
        return pd.read_csv(file_name)
    elif file_name.endswith(".xlsx"):
        return pd.read_excel(file_name)
    else:
        print("File not found")
        return None


def scatter_plot(data, x_label, y_label):
    plt.scatter(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Scatter Plot of {x_label} vs {y_label}')
    plt.show()


def calculate_mean(data):
    return np.mean(data)


def calculate_median(data):
    return np.median(data)


def calculate_std(data):
    return np.std(data)


def calculate_variance(data):
    return np.var(data)


def calculate_regression_line(data, x_label, y_label):
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(data[x_label], data[y_label])
    return slope, intercept


def draw_reg_line(data, x_label, y_label):
    slope, intercept = calculate_regression_line(data, x_label, y_label)

    plt.scatter(data[x_label], data[y_label])
    plt.plot(data[x_label], slope * data[y_label] + intercept, color = 'red', label = 'reg line')

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(f"Regression line {x_label} vs {y_label}")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    file_name = "results.csv"
    x_label = "Hindi"
    y_label = "English"

    data = read_file(file_name)

    scatter_plot(data, x_label, y_label)

    mean_value = calculate_mean(data)

    median_value = calculate_median(data)

    std_deviation = calculate_std(data)

    variance_value = calculate_variance(data)

    draw_reg_line(data, x_label, y_label)

    print(f"Mean: {mean_value}")