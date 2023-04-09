# import pandas as pd
# import numpy as np
# from numba import jit


# @jit(nopython=True)
# def process_pair(x1, y1, m, fuck9_values):
#     if np.isnan(fuck9_values[0]) or np.isnan(fuck9_values[1]) or np.isnan(fuck9_values[2]):
#         return

#     if fuck9_values[0] >= 0:
#         if fuck9_values[0] <= fuck9_values[1] and fuck9_values[0] <= fuck9_values[2]:
#             m[x1, y1] = 1

#     if fuck9_values[0] < 0:
#         if fuck9_values[0] <= fuck9_values[2] and fuck9_values[0] <= fuck9_values[1]:
#             m[x1, y1] = 1


# # Read CSV file and preprocess the data
# fuck7 = pd.read_csv("finally.csv")
# fuck7['datadate'] = pd.to_datetime(fuck7['datadate'])
# fuck7 = fuck7.sort_values(by='datadate').drop(columns=['X'])

# # Filter data by date
# # fuck8 = fuck7[fuck7['datadate'] == '2023-03-24']
# fuck8 = fuck7.query('datadate == "2023-03-24"')

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

#     x1 = fuck8.columns.get_loc(i) - 1
#     y1 = fuck8.columns.get_loc(j) - 1

#     stock1 = fuck8.columns.get_loc(f"{i}r")
#     stock2i = fuck8.columns.get_loc(f"{j}ryi")
#     stock2s = fuck8.columns.get_loc(f"{j}rys")
#     fuck9_values = fuck8.iloc[0, [stock1, stock2i, stock2s]].values

#     process_pair(x1, y1, m, fuck9_values)
##########################################
# import pandas as pd
# from datetime import datetime

# # Read the CSV file
# fuck7 = pd.read_csv("finally.csv")

# # Convert datadate to datetime and sort
# fuck7["datadate"] = pd.to_datetime(fuck7["datadate"])
# fuck7 = fuck7.sort_values(by="datadate")

# # Remove the 'X' column
# fuck7 = fuck7.drop(columns=["X"])

# # Filter the data
# fuck8 = fuck7[fuck7["datadate"] == datetime.strptime("2023-03-24", "%Y-%m-%d")]

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

#         x1 = fuck8.columns.get_loc(i) - 1
#         y1 = fuck8.columns.get_loc(j) - 1

#         stock1_colname = f"{i}r"
#         stock2i_colname = f"{j}ryi"
#         stock2s_colname = f"{j}rys"

#         fuck9 = fuck8[[stock1_colname, stock2i_colname, stock2s_colname]]

#         if fuck9.iloc[0].isnull().any():
#             continue

#         stock1_value = fuck9.iloc[0][stock1_colname]
#         stock2i_value = fuck9.iloc[0][stock2i_colname]
#         stock2s_value = fuck9.iloc[0][stock2s_colname]

#         if stock1_value >= 0:
#             if stock1_value <= stock2i_value and stock1_value <= stock2s_value:
#                 m[x1][y1] = 1
#         elif stock1_value < 0:
#             if stock1_value <= stock2s_value and stock1_value <= stock2i_value:
#                 m[x1][y1] = 1

import pandas as pd
from datetime import datetime

# Read the CSV file
fuck7 = pd.read_csv("finally.csv")

# Convert datadate to datetime and sort
fuck7["datadate"] = pd.to_datetime(fuck7["datadate"])
fuck7 = fuck7.sort_values(by="datadate")

# # Remove the 'X' column
# fuck7 = fuck7.drop(columns=["X"])

# Filter the data
fuck8 = fuck7[fuck7["datadate"] == datetime.strptime("2023-03-24", "%Y-%m-%d")]

# Create an empty matrix
m = [[0 for _ in range(497)] for _ in range(497)]

# Read newstocks.txt
with open("newstocks.txt", "r") as f:
    x = f.read().splitlines()

x[0] = "MMM"

# Loop through the stocks
for i in x:
    for j in x:
        print(f"{i} {j}")

        x1 = fuck8.columns.get_loc(i) - 1
        y1 = fuck8.columns.get_loc(j) - 1

        stock1 = fuck8.columns.get_loc(f"{i}r")
        stock2i = fuck8.columns.get_loc(f"{j}ryi")
        stock2s = fuck8.columns.get_loc(f"{j}rys")

        fuck9 = fuck8[[stock1, stock2i, stock2s]]

        if fuck9.iloc[0].isnull().any():
            continue

        if fuck9.iloc[0][stock1] >= 0:
            if fuck9.iloc[0][stock1] <= fuck9.iloc[0][stock2i] and fuck9.iloc[0][stock1] <= fuck9.iloc[0][stock2s]:
                m[x1][y1] = 1
        elif fuck9.iloc[0][stock1] < 0:
            if fuck9.iloc[0][stock1] <= fuck9.iloc[0][stock2s] and fuck9.iloc[0][stock1] <= fuck9.iloc[0][stock2i]:
                m[x1][y1] = 1


# # # import pandas as pd
# # # from datetime import datetime

# # # # Read the CSV file
# # # fuck7 = pd.read_csv("finally.csv")

# # # # Convert datadate to datetime and sort
# # # fuck7["datadate"] = pd.to_datetime(fuck7["datadate"])
# # # fuck7 = fuck7.sort_values(by="datadate")

# # # # # Remove the 'X' column
# # # # fuck7 = fuck7.drop(columns=["X"])

# # # # Filter the data
# # # fuck8 = fuck7[fuck7["datadate"] == datetime.strptime("2023-03-24", "%Y-%m-%d")]

# # # # Select specific columns
# # # fuck9 = fuck8[["AMZNr", "MSFTryi", "MSFTrys"]]

# # # # Create an empty matrix
# # # m = [[0 for _ in range(497)] for _ in range(497)]

# # # # Get the column indices for AMZN and MSFT
# # # x = fuck8.columns.get_loc("AMZN") - 1
# # # y = fuck8.columns.get_loc("MSFT") - 1

# # # # Check condition and update matrix value
# # # if (fuck9.iloc[0]["AMZNr"] <= fuck9.iloc[0]["MSFTryi"]) and (fuck9.iloc[0]["AMZNr"] <= fuck9.iloc[0]["MSFTrys"]):
# # #     m[x][y] = 1

# # # print(m[x][y])
