from datetime import datetime
import pandas as pd
import numpy as np
import numba
from numba import njit
from numba.typed import Dict
from numba.typed import List


@njit
def process_pair(fv8, n, x, total_pairs):
    m = np.zeros((498, 498))

    for index in range(total_pairs):
        i = x[index // n]
        j = x[index % n]
        # print('index', index)

        print(f"{i} {j}")

        x1 = x.index(i)
        y1 = x.index(j)
        fv10_values = np.array(
            [fv8[f"{i}r"], fv8[f"{j}ryi"], fv8[f"{j}rys"]])

        # x1 = fv8.columns.get_loc(i) - 1
        # y1 = fv8.columns.get_loc(j) - 1

        # stock1 = fv8.columns.get_loc(f"{i}r")
        # stock2i = fv8.columns.get_loc(f"{j}ryi")
        # stock2s = fv8.columns.get_loc(f"{j}rys")
        # fv9_values = fv8.iloc[0, [stock1, stock2i, stock2s]].values
        # fv10_values = np.array(
        #     [fv9_values[0], fv9_values[1], fv9_values[2]],  dtype=np.float64)
        # # ([stock1, stock2i, stock2s], dtype=np.float64)

        # process_pair(x1, y1, m, fv10_values)
        if (np.isnan(fv10_values[0]) or np.isnan(fv10_values[1]) or np.isnan(fv10_values[2])):
            continue

        if (fv10_values[0] >= 0):
            if fv10_values[0] <= fv10_values[1] and fv10_values[0] <= fv10_values[2]:
                m[x1][y1] = 1

        if (fv10_values[0] < 0):
            if fv10_values[0] <= fv10_values[2] and fv10_values[0] <= fv10_values[1]:
                m[x1][y1] = 1
    print('m', m)


# Read CSV file and preprocess the data
fv7 = pd.read_csv("finally.csv")
fv7['datadate'] = pd.to_datetime(fv7['datadate'])
fv7 = fv7.sort_values(by='datadate')


typed_dict = Dict.empty(
    key_type=numba.types.unicode_type,
    value_type=numba.types.float64
)


# Filter data by date
# fv8 = fv7[fv7['datadate'] == '2023-03-24']
# fv8 = fv7.query('datadate == "2023-03-24"').to_dict()
fv8 = fv7[fv7["datadate"] == datetime.strptime(
    "2023-03-24", "%Y-%m-%d")]

fv8 = fv8.drop("datadate", axis=1)
fv8 = fv8.drop("Unnamed: 0", axis=1)

fv8 = fv8.to_dict()
# print(fv8)

for key, value in fv8.items():
    typed_dict[key] = value[3328]

# print(typed_dict)

# Initialize the matrix and stock symbols list
with open("newstocks.txt", "r") as f:
    x = f.read().splitlines()
x[0] = "A"

# Replace the double for loop with a single loop
n = len(x)
total_pairs = n * n
# print(total_pairs)
typed_x = List(x)

process_pair(typed_dict, n, typed_x, total_pairs)
# for index in range(total_pairs):
#     i = x[index // n]
#     j = x[index % n]

#     # print(f"{i} {j}")

#     x1 = fv8.columns.get_loc(i) - 1
#     y1 = fv8.columns.get_loc(j) - 1

#     stock1 = fv8.columns.get_loc(f"{i}r")
#     stock2i = fv8.columns.get_loc(f"{j}ryi")
#     stock2s = fv8.columns.get_loc(f"{j}rys")
#     fv9_values = fv8.iloc[0, [stock1, stock2i, stock2s]].values
#     fv10_values = np.array(
#         [fv9_values[0], fv9_values[1], fv9_values[2]],  dtype=np.float64)
#     # ([stock1, stock2i, stock2s], dtype=np.float64)


#     process_pair(x1, y1, m, fv10_values)
