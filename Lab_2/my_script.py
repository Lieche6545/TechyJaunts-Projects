import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_housing = pd.read_csv('Housing.csv')
print(df_housing.head())

print(df_housing.tail())

print(df_housing.info())

print(df_housing.shape)