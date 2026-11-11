import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Google Colab
# dataframe = pd.read_csv("/content/Zomato-data-.csv")

# Load the dataset locally
from pathlib import Path
dataframe = pd.read_csv(Path(__file__).with_name("Zomato-data-.csv"))

# Creating the dataframe
# print(dataframe.head())

# Data cleaning and Preparation
    # 1. Convert the rate column to a float by removing denominator values
def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

    # 2. Getting a summary of the dataframe use df.info()
# dataframe.info()

    # 3. Checking for missing or null values to identify any data gaps.
print(dataframe.isnull().sum())

# Exploring Restaurant Types
    # 1. Let's see the listed_in (type) column to identify popular restaurant categories.
    