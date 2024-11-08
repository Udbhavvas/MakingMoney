import pandas as pd
from datetime import datetime

# Read the CSV file
fv7 = pd.read_csv("finally.csv")

# Convert datadate to datetime and sort
fv7["datadate"] = pd.to_datetime(fv7["datadate"])
fv7 = fv7.sort_values(by="datadate")

# # Remove the 'X' column
# fv7 = fv7.drop(columns=["X"])

# Filter the data
fv8 = fv7[fv7["datadate"] == datetime.strptime("2023-03-24", "%Y-%m-%d")]

# Create an empty matrix
m = [[0 for _ in range(498)] for _ in range(498)]
# m = np.zeros((497, 497))

# Read newstocks.txt
with open("newstocks.txt", "r") as f:
    x = f.read().splitlines()

x[0] = "MMM"

# Loop through the stocks
for i in x:
    for j in x:
        print(f"{i} {j}")

        x1 = fv8.columns.get_loc(i)-1
        y1 = fv8.columns.get_loc(j)-1

        # stock1 = fv8.columns.get_loc(f"{i}r")
        # stock2i = fv8.columns.get_loc(f"{j}ryi")
        # stock2s = fv8.columns.get_loc(f"{j}rys")
        # f"{stock1, stock2i, stock2s}"
        # fv8.iloc

        fv9 = fv8[[f"{i}r", f"{j}ryi", f"{j}rys"]]

        if fv9.iloc[0].isnull().any():
            continue

        if fv9.iloc[0][0] >= 0:
            if fv9.iloc[0][0] <= fv9.iloc[0][1] and fv9.iloc[0][0] <= fv9.iloc[0][2]:
                m[x1][y1] = 1
        elif fv9.iloc[0][0] < 0:
            if fv9.iloc[0][0] <= fv9.iloc[0][2] and fv9.iloc[0][0] <= fv9.iloc[0][1]:
                m[x1][y1] = 1


# import pandas as pd
# import numpy as np
# from numba import jit


# @jit(nopython=True)
# def process_pair(x1, y1, m, fv9_values):
#     if np.isnan(fv9_values[0]) or np.isnan(fv9_values[1]) or np.isnan(fv9_values[2]):
#         return

#     if fv9_values[0] >= 0:
#         if fv9_values[0] <= fv9_values[1] and fv9_values[0] <= fv9_values[2]:
#             m[x1, y1] = 1

#     if fv9_values[0] < 0:
#         if fv9_values[0] <= fv9_values[2] and fv9_values[0] <= fv9_values[1]:
#             m[x1, y1] = 1


# # Read CSV file and preprocess the data
# fv7 = pd.read_csv("finally.csv")
# fv7['datadate'] = pd.to_datetime(fv7['datadate'])
# fv7 = fv7.sort_values(by='datadate').drop(columns=['X'])

# # Filter data by date
# # fv8 = fv7[fv7['datadate'] == '2023-03-24']
# fv8 = fv7.query('datadate == "2023-03-24"')

# # Initialize the matrix and stock symbols list
# m = np.zeros((497, 497))
# with open("newstocks.txt", "r") as f:
#     x = f.read().splitlines()
# x[0] = "MMM"

# # Replace the double for loop with a single loop
# n = len(x)
# total_pairs = n * n
# for index in range(total_pairs):
#     i = x[index // n]
#     j = x[index % n]

#     print(f"{i} {j}")

#     x1 = fv8.columns.get_loc(i) - 1
#     y1 = fv8.columns.get_loc(j) - 1

#     stock1 = fv8.columns.get_loc(f"{i}r")
#     stock2i = fv8.columns.get_loc(f"{j}ryi")
#     stock2s = fv8.columns.get_loc(f"{j}rys")
#     fv9_values = fv8.iloc[0, [stock1, stock2i, stock2s]].values

#     process_pair(x1, y1, m, fv9_values)
##########################################
# import pandas as pd
# from datetime import datetime

# # Read the CSV file
# fv7 = pd.read_csv("finally.csv")

# # Convert datadate to datetime and sort
# fv7["datadate"] = pd.to_datetime(fv7["datadate"])
# fv7 = fv7.sort_values(by="datadate")

# # Remove the 'X' column
# fv7 = fv7.drop(columns=["X"])

# # Filter the data
# fv8 = fv7[fv7["datadate"] == datetime.strptime("2023-03-24", "%Y-%m-%d")]

# # Create an empty matrix
# m = [[0 for _ in range(497)] for _ in range(497)]

# # Read newstocks.txt
# with open("newstocks.txt", "r") as f:
#     x = f.read().splitlines()

# x[0] = "MMM"

# # Loop through the stocks
# for i in x:
#     for j in x:
#         print(f"{i} {j}")

#         x1 = fv8.columns.get_loc(i) - 1
#         y1 = fv8.columns.get_loc(j) - 1

#         stock1_colname = f"{i}r"
#         stock2i_colname = f"{j}ryi"
#         stock2s_colname = f"{j}rys"

#         fv9 = fv8[[stock1_colname, stock2i_colname, stock2s_colname]]

#         if fv9.iloc[0].isnull().any():
#             continue

#         stock1_value = fv9.iloc[0][stock1_colname]
#         stock2i_value = fv9.iloc[0][stock2i_colname]
#         stock2s_value = fv9.iloc[0][stock2s_colname]

#         if stock1_value >= 0:
#             if stock1_value <= stock2i_value and stock1_value <= stock2s_value:
#                 m[x1][y1] = 1
#         elif stock1_value < 0:
#             if stock1_value <= stock2s_value and stock1_value <= stock2i_value:
#                 m[x1][y1] = 1
