import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: The loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def save_plot(fig, file_path):
    """
    Save a matplotlib figure to a file.
    
    Parameters:
    fig (Figure): The matplotlib figure to save.
    file_path (str): The path to save the figure.
    """
    fig.savefig(file_path)

def plot_data(data, x_col, y_col, title="Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Plot data using seaborn.
    
    Parameters:
    data (DataFrame): The data to plot.
    x_col (str): The column to use for the x-axis.
    y_col (str): The column to use for the y-axis.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    
    Returns:
    Figure: The created matplotlib figure.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    fig = plt.gcf()
    return fig

def describe_data(data):
    """
    Generate descriptive statistics of the data.
    
    Parameters:
    data (DataFrame): The data to describe.
    
    Returns:
    DataFrame: The descriptive statistics.
    """
    return data.describe()

def check_missing_values(data):
    """
    Check for missing values in the data.
    
    Parameters:
    data (DataFrame): The data to check.
    
    Returns:
    Series: The count of missing values for each column.
    """
    return data.isnull().sum()