import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
#
# # Try different encodings to read the CSV file
# encodings = ['utf-8', 'latin1', 'ISO-8859-1']
#
# for encoding in encodings:
#     try:
#         data = pd.read_csv("sales_data_sample.csv", encoding=encoding)
#         break  # If successful, exit the loop
#     except UnicodeDecodeError:
#         print(f"Failed to read with encoding: {encoding}")
#
# # Data exploration
# print(data.head())  # Display the first few rows
# print(data.info())  # Check data types and missing values
# print(data.describe())  # Summary statistics for numerical columns
#
# # Handle missing values using Scikit-Learn SimpleImputer
# numeric_columns = data.select_dtypes(include=[float, int]).columns
# categorical_columns = data.select_dtypes(include=['object']).columns
#
# numeric_imputer = SimpleImputer(strategy='mean')
# data[numeric_columns] = numeric_imputer.fit_transform(data[numeric_columns])
#
# # Encoding categorical data using Scikit-Learn LabelEncoder
# label_encoder = LabelEncoder()
# for col in categorical_columns:
#     data[col] = label_encoder.fit_transform(data[col])
#
# # Feature scaling using Scikit-Learn StandardScaler for numeric columns
# scaler = StandardScaler()
# data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
#
# # Remove duplicates
# data.drop_duplicates(inplace=True)
#
# # Select specific columns of interest
# selected_columns = data[['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'CUSTOMERNAME']]
#
# # Filter data based on conditions (e.g., select data for a specific year)
# filtered_data = data[data['YEAR_ID'] == 2022]
#
# # Rename columns for clarity
# data.rename(columns={'ORDERNUMBER': 'OrderNumber', 'QUANTITYORDERED': 'QuantityOrdered'}, inplace=True)
#
# # Export the cleaned dataset to a new CSV file
# data.to_csv("cleaned_sales_data.csv", index=False)
import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Sort the ages list in ascending order and store the result in a new list
sorted_ages = sorted(ages)

# Calculate the 75th percentile using numpy
x = numpy.percentile(sorted_ages, 75)

print(sorted_ages)  # Sorted ages list
print(x)           # 75th percentile
