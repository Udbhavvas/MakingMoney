from datetime import datetime
import pandas as pd
import numpy as np
import numba
from numba import njit
from numba.typed import Dict
from numba.typed import List


@njit
def process_pair(fuck8, n, x, total_pairs):
    m = np.zeros((498, 498))

    for index in range(total_pairs):
        i = x[index // n]
        j = x[index % n]
        # print('index', index)

        print(f"{i} {j}")

        x1 = x.index(i)
        y1 = x.index(j)
        fuck10_values = np.array(
            [fuck8[f"{i}r"], fuck8[f"{j}ryi"], fuck8[f"{j}rys"]])

        # x1 = fuck8.columns.get_loc(i) - 1
        # y1 = fuck8.columns.get_loc(j) - 1

        # stock1 = fuck8.columns.get_loc(f"{i}r")
        # stock2i = fuck8.columns.get_loc(f"{j}ryi")
        # stock2s = fuck8.columns.get_loc(f"{j}rys")
        # fuck9_values = fuck8.iloc[0, [stock1, stock2i, stock2s]].values
        # fuck10_values = np.array(
        #     [fuck9_values[0], fuck9_values[1], fuck9_values[2]],  dtype=np.float64)
        # # ([stock1, stock2i, stock2s], dtype=np.float64)

        # process_pair(x1, y1, m, fuck10_values)
        if (np.isnan(fuck10_values[0]) or np.isnan(fuck10_values[1]) or np.isnan(fuck10_values[2])):
            continue

        if (fuck10_values[0] >= 0):
            if fuck10_values[0] <= fuck10_values[1] and fuck10_values[0] <= fuck10_values[2]:
                m[x1][y1] = 1

        if (fuck10_values[0] < 0):
            if fuck10_values[0] <= fuck10_values[2] and fuck10_values[0] <= fuck10_values[1]:
                m[x1][y1] = 1
    print('m', m)


# Read CSV file and preprocess the data
fuck7 = pd.read_csv("finally.csv")
fuck7['datadate'] = pd.to_datetime(fuck7['datadate'])
fuck7 = fuck7.sort_values(by='datadate')


typed_dict = Dict.empty(
    key_type=numba.types.unicode_type,
    value_type=numba.types.float64
)


# Filter data by date
# fuck8 = fuck7[fuck7['datadate'] == '2023-03-24']
# fuck8 = fuck7.query('datadate == "2023-03-24"').to_dict()
fuck8 = fuck7[fuck7["datadate"] == datetime.strptime(
    "2023-03-24", "%Y-%m-%d")]

fuck8 = fuck8.drop("datadate", axis=1)
fuck8 = fuck8.drop("Unnamed: 0", axis=1)

fuck8 = fuck8.to_dict()
# print(fuck8)

for key, value in fuck8.items():
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

#     x1 = fuck8.columns.get_loc(i) - 1
#     y1 = fuck8.columns.get_loc(j) - 1

#     stock1 = fuck8.columns.get_loc(f"{i}r")
#     stock2i = fuck8.columns.get_loc(f"{j}ryi")
#     stock2s = fuck8.columns.get_loc(f"{j}rys")
#     fuck9_values = fuck8.iloc[0, [stock1, stock2i, stock2s]].values
#     fuck10_values = np.array(
#         [fuck9_values[0], fuck9_values[1], fuck9_values[2]],  dtype=np.float64)
#     # ([stock1, stock2i, stock2s], dtype=np.float64)


#     process_pair(x1, y1, m, fuck10_values)
